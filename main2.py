from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from base import llm
from prompts.prompts import *
import time
from utils.utils import string2list
from utils.template import rz_action_template_lf_window
from scenecombo.summary import scenario_config

from FuzzyInstruction.FuzzyInstruction import fuzzy_scene_generate_actual_scene

from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast, BertForSequenceClassification, BertTokenizerFast, BertTokenizer, BertModel, pipeline
import torch
import time
import logging

def generate_single_scenario(instruction, prompts):
    prompt = PromptTemplate(
        template=left_window_scene,
        input_variables=["query"]
    )
    chain = prompt | llm | StrOutputParser()
    scenario = chain.invoke({"instruction": instruction})
    return scenario

def main():
    model_path = "/home/ubuntu/iScenario/LLM_Assist/model"
    model = BertForSequenceClassification.from_pretrained(model_path)
    tokenizer = BertTokenizer.from_pretrained(model_path)
    nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    # TODO @qinxiaocheng TTS播放这段话
    AI_Chat = "AI: 您好，有什么可以帮您"
    print (AI_Chat)
    logging.info(AI_Chat)
    start = time.time()
    ''' 
    第一部分，ASR识别
    '''
    # TODO @qinxiaocheng ASR用户指令
    instruction = "我很热"
    print (f"Human: {instruction}")
    logging.info(f"Human: {instruction}")

    fuzzyscene = fuzzy_scene_generate_actual_scene(instruction)
    actual_scene = fuzzyscene.split(": ")[1]
    actual_scene = "打开左车窗一半"
    '''
    第二部分 意图识别
    '''
    label = nlp(actual_scene)[0]['label']
    scenario = scenario_config[label]
    print (f"Bert决策场景: {label}")
    logging.info(f"Bert决策场景: {label}")


    '''
    第三部分 场景生成
    '''
    json_params_list = string2list(generate_single_scenario(actual_scene, scenario.get("prompts")))
    name = json_params_list[0]
    args = [{
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
    json_params_config = rz_action_template_lf_window(name, args)
    print ("生成json \n {}".format(json_params_config))
    logging.info("生成json \n {}".format(json_params_config))


    end1 = time.time()

    value = json_params_config.get("args")[1]["value"]
    '''
    第四部分： TTS
    TODO @qinxiaocheng 播放response_sentence
    '''
    response_sentence = f"为您推荐{actual_scene}, " + scenario.get("response")[2].format(scenario[value])
    print ("AI: {}".format(response_sentence))
    logging.info(f"AI: {response_sentence}")
    print(f"Execution time: {end1 - start} seconds")
    


if __name__ == "__main__":
    main()