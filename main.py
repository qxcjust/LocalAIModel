from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from base import llm
from prompts.prompts import *
import time
from utils.utils import string2list, string2string
from utils.template import rz_action_template_lf_window
from scenecombo.summary import scenario_config_all

from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast, BertForSequenceClassification, BertTokenizerFast, BertTokenizer, BertModel, pipeline
import torch
import logging
from FuzzyInstruction.FuzzyInstruction import fuzzy_scene_generate_actual_scene

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

    # 场景生成
    json_params_list = string2list(generate_single_scenario(instruction, scenario.get("prompts")))
    name = json_params_list[0]
    args = [
        {
            "name": json_params_list[1],
            "type": json_params_list[1],
            "value": json_params_list[2]
        },
        {
            "name": json_params_list[3],
            "type": json_params_list[3],
            "value": json_params_list[4]
        }
    ]
    #json_params_config = rz_action_template_lf_window(name, args)
    json_params_config = rz_action_template_lf_window(name, args, label)
    logging.info("生成json \n {}".format(json_params_config))

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

