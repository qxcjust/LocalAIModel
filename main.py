from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from base import llm, llm_generate,llm_tts_generate
from prompts.prompts import *
import time
from utils.utils import string2list, string2string, config_args, match_fuzzy_instruction, generate_response_sentence, extract_identifier_content
from utils.template import rz_action_template_lf_window
from scenecombo.summary import scenario_config_all

from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast, BertForSequenceClassification, BertTokenizerFast, BertTokenizer, BertModel, pipeline
import torch
import logging
from FuzzyInstruction.FuzzyInstruction import fuzzy_scene_generate_actual_scene
from scenecombo.FuzzyInstructionScene import FuzzyInstruction

from FuzzyInstruction.FuzzyInstruction import fuzzy_scene_generate_actual_scene
from prompts.scenepromptselect import select_scene_prompt

from predict import load_model, generate_tts, predict

### base fastapi add interfase
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
import asyncio
import json
from Cache.action_config import action_configs

from pydantic import BaseModel
from Cache.action_config import action_configs
import difflib
from prompts.scenepromptselect import select_scene_prompt

app = FastAPI()

class InstructionInput(BaseModel):
    instruction: str

def get_closest_match(label, scenario_config_all):
    # 获取所有配置项的键
    scenario_keys = list(scenario_config_all.keys())
    # 使用difflib的get_close_matches方法来寻找最接近的匹配项
    closest_matches = difflib.get_close_matches(label, scenario_keys, n=1, cutoff=0.6)
    # 如果找到了匹配项，则返回对应的配置项，否则返回None
    if closest_matches:
        return scenario_config_all[closest_matches[0]]
    else:
        return None

def generate_single_scenario(instruction, prompts):
    prompt = PromptTemplate(
        template=prompts,
        # input_variables=["query"]
    )
    chain = prompt | llm_generate | StrOutputParser()
    print(f"Instruction from User: {instruction}")
    scenario = chain.invoke({"instruction": instruction})
    print (scenario)
    return scenario

def Albert_scenario_select(instruction):
    prompt = PromptTemplate(
        template=select_scene_prompt,
        # input_variables=["query"]
    )
    chain = prompt | llm | StrOutputParser()
    scenario = chain.invoke({"instruction": instruction})
    return scenario

# 全局变量用于存储识别结果
global_result = ""
result_event = asyncio.Event()


@app.get("/process_syncLLMResult")
async def syncLLMResult(request: Request):
    async def event_generator():
        global global_result
        while True:
            # 等待新结果
            await result_event.wait()
            result_event.clear()
            yield {"data": global_result}
            # await asyncio.sleep(0.1)  # 避免频繁发送

    return EventSourceResponse(event_generator())

def generate_result(response, actions, sequence_id):
    # 创建一个字典，代表JSON对象
    # sequence_id: 0x01，0xff（ff意味着结束会话）
    json_data = {
        "response": response,
        "actions": actions,
        "sequence_id":sequence_id
    }
    json_string = json.dumps(json_data, ensure_ascii=False)
    print(json_string)
    return json_string

def send_client_message(response,actions,sequence_id):
    global global_result
    actions_list = []
    for scene_action in actions:
        actions_list.append(scene_action[1])
    global_result = generate_result(response,actions_list,sequence_id)
    result_event.set()  # 通知 SSE 有新结果

@app.post("/process_instruction")
async def process_instruction(input: InstructionInput):
    loaded_model = load_model()

    instruction = input.instruction
    print(f"Human: {instruction}")
    start = time.time()
    # 意图识别
    #model_path = "/home/ubuntu/iScenario/LLM_Assist/model"
    #model = BertForSequenceClassification.from_pretrained(model_path)
    #tokenizer = BertTokenizer.from_pretrained(model_path)
    #nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    #label = nlp(instruction)[0]['label']
    label = string2string(Albert_scenario_select(instruction)).replace(' ', '')
    print (label)
    if label == "温度控制场景":
        label = "空调控制场景"
    scenario = get_closest_match(label,scenario_config_all)
    print(f"场景决策: {label}")
    end1 = time.time()
    print(f"场景决策 Execution time: {end1 - start} seconds")

    # 返回值
    action_list = []
    if label != '模糊场景':
        # 场景生成
        json_params_list = string2list(extract_identifier_content(generate_single_scenario(instruction, scenario.get("prompts"))))

        # 生成场景json
        name = json_params_list[0]
        args = config_args(json_params_list)

        end2 = time.time()
        logging.info(f"场景生成 Execution time: {end2 - end1} seconds")
        print(f"场景生成json: {end2 - end1}")
        json_params_config = rz_action_template_lf_window(name, args, label)
        print("生成json \n {}".format(json_params_config))

        print(f"Execution time: {end2 - start} seconds")

        response_sentence, checkStatus = generate_response_sentence(label, json_params_config, scenario, json_params_list, name)
        print(response_sentence)
        # 如果返回的是True，说明是重复的指令，不需要再次执行
        if checkStatus == True:
            pass
        else:
            action_list.append(json_params_config)

        print(f"Assistant: {response_sentence}")
        end1 = time.time()
        print({
            "scenario_decision": label,
            "json_config": action_list,
            "response": response_sentence
        })
        return {
            "scenario_decision": label,
            "json_config": action_list,
            "response": response_sentence
        }
    else:
        # 返回值
        action_list = []

        # all_scenario = scenario.keys()
        # matched_scenario = match_fuzzy_instruction(instruction, all_scenario)

        # actions = scenario[matched_scenario]['action'].split(',')

        # TODO 并行tts合成和执行
        start3 = time.time()
        actions = predict(loaded_model, instruction)
        end3 = time.time()
        
        action_lists_str = ", ".join(actions)
        # print (generate_tts(instruction, action_lists_str))
        fuzzy_reponse = extract_identifier_content(generate_tts(instruction, action_lists_str))
        
        
        print(f"ML Model: {end3 - start3} seconds")
        # 缓慢播放，等待生成完成
        # response_sentence = scenario[matched_scenario]['response']

        print(f"Assistant: {fuzzy_reponse}")
        logging.info(f"Assistant: {fuzzy_reponse}")

        for action in actions:
            #子场景决策
            if action in action_configs:
                action_list.append(action_configs[action])
            else:
                print (f"子指令： {action}")
                sub_label = string2string(Albert_scenario_select(action)).replace(' ', '')
                if sub_label == "温度控制场景":
                    sub_label = "空调控制场景"
                sub_scenario = scenario_config_all[sub_label]
                print(f"子场景决策: {sub_label}")
                logging.info(f"子场景决策: {sub_label}")

                #子场景生成
                sub_json_params_list = string2list(extract_identifier_content(generate_single_scenario(action, sub_scenario.get("prompts"))))
                sub_name = sub_json_params_list[0]

                # TODO qinxiaocheng
                sub_args = config_args(sub_json_params_list)
                sub_json_params_config = rz_action_template_lf_window(sub_name, sub_args, sub_label)
                print("子生成json \n {}".format(sub_json_params_list))
                logging.info("子生成json \n {}".format(sub_json_params_config))

                action_configs[action] = sub_json_params_list
                # with open('Cache/action_config.py', 'w') as f:
                #     f.write(action_configs)
                # f.close()

                action_list.append(sub_json_params_config)
        print (f"生成全部json: \n{action_list}")
        end3 = time.time()
        print(f"Total Execution time: {end3 - start} seconds")
        return {
            "scenario_decision": label,
            "json_config": action_list,
            "response": fuzzy_reponse
        }

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8088)
