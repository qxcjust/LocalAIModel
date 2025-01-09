from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from base import llm
from prompts.prompts import *
import time
from utils.utils import string2list, string2string, config_args, match_fuzzy_instruction
from utils.template import rz_action_template_lf_window
from scenecombo.summary import scenario_config_all

from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast, BertForSequenceClassification, BertTokenizerFast, BertTokenizer, BertModel, pipeline
import torch
import logging
from FuzzyInstruction.FuzzyInstruction import fuzzy_scene_generate_actual_scene
from scenecombo.FuzzyInstructionScene import FuzzyInstruction

### base fastapi add interfase
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class InstructionInput(BaseModel):
    instruction: str

def generate_single_scenario(instruction, prompts):
    prompt = PromptTemplate(
        template=prompts,
        input_variables=["query"]
    )
    chain = prompt | llm | StrOutputParser()
    scenario = chain.invoke({"instruction": instruction})
    print (scenario)
    return scenario

def Albert_scenario_select(instruction):
    prompt = PromptTemplate(
        template=select_scene_prompt,
        input_variables=["query"]
    )
    chain = prompt | llm | StrOutputParser()
    scenario = chain.invoke({"instruction": instruction})
    return scenario

@app.post("/process_instruction")
async def process_instruction(input: InstructionInput):
    instruction = input.instruction
    logging.info(f"Human: {instruction}")
    start = time.time()
    # 意图识别
    #model_path = "/home/ubuntu/iScenario/LLM_Assist/model"
    #model = BertForSequenceClassification.from_pretrained(model_path)
    #tokenizer = BertTokenizer.from_pretrained(model_path)
    #nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    #label = nlp(instruction)[0]['label']
    label = string2string(Albert_scenario_select(instruction)).replace(' ', '')
    scenario = scenario_config_all[label]
    logging.info(f"场景决策: {label}")

    if label == '模糊场景':
        # 返回值
        action_list = []

        all_scenario = scenario.keys()
        matched_scenario = match_fuzzy_instruction(instruction, all_scenario)

        actions = scenario[matched_scenario]['action'].split(',')

        # 缓慢播放，等待生成完成
        response_sentence = scenario[matched_scenario]['response']

        print(f"Assistant: {response_sentence}")
        logging.info(f"Assistant: {response_sentence}")

        for action in actions:
            #子场景决策

            print (f"子指令： {action}")
            sub_label = string2string(Albert_scenario_select(action)).replace(' ', '')
            sub_scenario = scenario_config_all[sub_label]
            print(f"子场景决策: {sub_label}")
            logging.info(f"子场景决策: {sub_label}")

            #子场景生成
            sub_json_params_list = string2list(generate_single_scenario(action, sub_scenario.get("prompts")))
            sub_name = sub_json_params_list[0]

            # TODO qinxiaocheng
            sub_args = config_args(sub_json_params_list)
            sub_json_params_config = rz_action_template_lf_window(sub_name, sub_args, sub_label)
            print("子生成json \n {}".format(sub_json_params_list))
            logging.info("子生成json \n {}".format(sub_json_params_config))

            action_list.append(sub_json_params_config)
        print (f"生成全部json: \n{action_list}")
        end2 = time.time()
        print(f"Execution time: {end2 - start} seconds")
        return {
            "scenario_decision": label,
            "json_config": action_list,
            "response": response_sentence
        }
    else:
        # 场景生成
        json_params_list = string2list(generate_single_scenario(instruction, scenario.get("prompts")))
        name = json_params_list[0]
        args = config_args(json_params_list)
        json_params_config = rz_action_template_lf_window(name, args, label)
        logging.info("生成json \n {}".format(json_params_config))

        value = ''
        if len(json_params_list) == 3:
            value = json_params_config.get("args")[0]["value"]
        else:
            value = json_params_config.get("args")[1]["value"]
        
        response_sentence = scenario.get("response")[0].format(scenario[value])
        logging.info(f"Assistant: {response_sentence}")
        end1 = time.time()
        print(f"Execution time: {end1 - start} seconds")
        return {
            "scenario_decision": label,
            "json_config": json_params_config,
            "response": response_sentence
        }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    import uvicorn
    uvicorn.run(app, host="localhost", port=8088)

