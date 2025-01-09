import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def string2list(string_list):
    temp = string_list.split(', ')
    return temp


def string2string(string_list):
    temp = string_list.split('返回：')
    return temp[-1]

def config_args(json_params_list):
    length_json_params = len(json_params_list)
    if length_json_params == 3:
        args = [
            {
            "name": json_params_list[1],
            "type": json_params_list[1],
            "value": json_params_list[2]
            }
        ]
        return args
    elif length_json_params == 5:
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
        return args
    else:
        # TODO error deal
        print ('length error')  

def match_fuzzy_instruction(instruction, instructions):
    temp = 0
    returntext = ""
    for inst in instructions:
        vectorize = CountVectorizer()
        vectors = vectorize.fit_transform([instruction, inst])
        similarity_score = cosine_similarity(vectors)[0][1]
        if similarity_score >= temp:
            returntext = inst
            similarity_score = temp
    return returntext

def generate_response_sentence(label, json_params_config, scenario, json_params_list, name):
    if label == '车外灯':
        value = ''
        if len(json_params_list) == 3:
            value = json_params_config.get("args")[0]["value"]
        else:
            value = json_params_config.get("args")[1]["value"]
        response_sentence = scenario.get("response")[0].format(scenario[name], scenario[value])
        return response_sentence
    else:
        value = ''
        if len(json_params_list) == 3:
            value = json_params_config.get("args")[0]["value"]
        else:
            value = json_params_config.get("args")[1]["value"]
        response_sentence = scenario.get("response")[0].format(scenario[value])
        return response_sentence
    
import re
 
def extract_identifier_content(text):
    # 正则表达式匹配两个井号之间的内容
    pattern = re.compile(r"#\s*(.*?)\s*#")
    match = pattern.search(text)
    if match:
        return match.group(1)
    else:
        return None


