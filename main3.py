from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from base import llm, llm_generate
from prompts.prompts import *
import time
from utils.utils import string2list, string2string, config_args, match_fuzzy_instruction, generate_response_sentence, extract_identifier_content
from utils.template import rz_action_template_lf_window
from scenecombo.summary import scenario_config_all

from scenecombo.FuzzyInstructionScene import FuzzyInstruction

from FuzzyInstruction.FuzzyInstruction import fuzzy_scene_generate_actual_scene
from prompts.scenepromptselect import select_scene_prompt

# from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast, BertForSequenceClassification, BertTokenizerFast, BertTokenizer, BertModel, pipeline
# import torch
import time
import logging
import difflib

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
        input_variables=["query"]
    )
    chain = prompt | llm_generate | StrOutputParser()
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

def main():
    instruction = "主驾按摩关闭"
    logging.info(f"Human: {instruction}")
    start = time.time()
    # 意图识别
    #model_path = "/home/ubuntu/iScenario/LLM_Assist/model"
    #model = BertForSequenceClassification.from_pretrained(model_path)
    #tokenizer = BertTokenizer.from_pretrained(model_path)
    #nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    #label = nlp(instruction)[0]['label']
    label = string2string(Albert_scenario_select(instruction)).replace(' ', '')
    scenario = get_closest_match(label,scenario_config_all)
    # scenario = get_closest_match(label, scenario_config_all)
    logging.info(f"场景决策: {label}")
    end1 = time.time()
    logging.info(f"场景决策 Execution time: {end1 - start} seconds")
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
        logging.info("生成json \n {}".format(json_params_config))

        print(f"Execution time: {end2 - start} seconds")

        response_sentence, checkStatus = generate_response_sentence(label, json_params_config, scenario, json_params_list, name)
        print(response_sentence)
        if checkStatus == True:
            pass
        else:
            action_list.append(json_params_config)

        logging.info(f"Assistant: {response_sentence}")
        end1 = time.time()
        return {
            "scenario_decision": label,
            "json_config": action_list,
            "response": response_sentence
        }
    else:
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
            sub_json_params_list = string2list(extract_identifier_content(generate_single_scenario(action, sub_scenario.get("prompts"))))
            sub_name = sub_json_params_list[0]

            # TODO qinxiaocheng
            sub_args = config_args(sub_json_params_list)
            sub_json_params_config = rz_action_template_lf_window(sub_name, sub_args, sub_label)
            print("子生成json \n {}".format(sub_json_params_list))
            logging.info("子生成json \n {}".format(sub_json_params_config))

            action_list.append(sub_json_params_config)
        print (f"生成全部json: \n{action_list}")
        end3 = time.time()
        print(f"Total Execution time: {end3 - start} seconds")
        return {
            "scenario_decision": label,
            "json_config": action_list,
            "response": response_sentence
        }

if __name__ == "__main__":
    main()