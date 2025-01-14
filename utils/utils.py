import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from VehicleStatus.checkstatus import Status

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
        if similarity_score > temp:
            returntext = inst
            similarity_score = temp
    return returntext

def generate_response_sentence(label, json_params_config, scenario, json_params_list, name):
    response_sentence = ""
    if label == '车门场景':
        if Status[label]['state'] == json_params_config['args'][1]['value']:
            valuetype = json_params_config.get('args')[0]['value']
            response_sentence = scenario['responseOpen'].format(scenario['DoorID'][valuetype])
            return response_sentence, True
        else:
            value = json_params_config.get("args")[1]["value"]
            valuetype = json_params_config.get('args')[0]['value']
            response_sentence = scenario.get("response")[0].format(scenario['DoorID'][value], scenario['DoorID'][valuetype])
            return response_sentence, False
    elif label == '氛围灯场景':
        if Status[label]['state'] == json_params_config['args'][0]['value']:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario['responseOpen'].format(scenario[value])
            return response_sentence, True
        else:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario.get("response")[0].format(scenario[value])
            return response_sentence, False        
    elif label == '车窗场景':
        if Status[label]['state'] == json_params_config['args'][1]['value']:
            valuetype = json_params_config.get('args')[0]['value']
            response_sentence = scenario['responseOpen'].format(scenario['WindowAreaID'][valuetype])
            return response_sentence, True
        else:
            value = ''
            valuetype = ''
            if len(json_params_list) == 3:
                value = json_params_config.get("args")[0]["value"]
                valuetype = json_params_config.get('args')[0]['value']
            else:
                value = json_params_config.get("args")[1]["value"]
                valuetype = json_params_config.get('args')[0]['value']
            # 0可以随机给
            response_sentence = scenario.get("response")[0].format(scenario[value], scenario['WindowAreaID'][valuetype])
            return response_sentence, False
    elif label == '座椅场景':
        if Status[label]['state'] == json_params_config['args'][1]['value']:
            valuetype = json_params_config.get('args')[0]['value']
            response_sentence = scenario['responseOpen'].format(scenario['chairmassage'][valuetype])
            return response_sentence, True
        else:
            if name == "setSeatMassageMode":
                value = json_params_config.get("args")[1]["value"]
                valuetype = json_params_config.get('args')[0]['value']
                response_sentence = scenario.get("response")[2].format(scenario['chairmassage'][value], scenario['chairmassage']['MassageMode'][valuetype])
            else:
                value = json_params_config.get("args")[1]["value"]
                valuetype = json_params_config.get('args')[0]['value']
                response_sentence = scenario.get("response")[0].format(scenario['chairadjust'][value], scenario['chairadjust']['SeatID'][valuetype])
            return response_sentence, False
    elif label == '后视镜场景':
        if Status[label]['state'] == json_params_config['args'][1]['value']:
            valuetype = json_params_config.get('args')[0]['value']
            value = json_params_config.get('args')[1]['value']
            response_sentence = scenario['responseOpen'].format(scenario['MirrorID'][valuetype], scenario[value])
            return response_sentence, True
        else:
            value = json_params_config.get("args")[1]["value"]
            valuetype = json_params_config.get('args')[0]['value']
            response_sentence = scenario.get("response")[0].format(scenario[value], scenario['MirrorID'][valuetype])
            return response_sentence, False
    elif label == '调光玻璃场景':
        if Status[label]['state'] == json_params_config['args'][1]['value']:
            valuetype = json_params_config.get('args')[0]['value']
            value = json_params_config.get('args')[1]['value']
            response_sentence = scenario['responseOpen'].format(scenario['GlassID'][valuetype], scenario[value])
            return response_sentence, True
        else:
            value = json_params_config.get("args")[1]["value"]
            valuetype = json_params_config.get('args')[0]['value']
            response_sentence = scenario.get("response")[0].format(scenario[value], scenario['GlassID'][valuetype])
            return response_sentence, False
    elif label == '播放音乐场景':
        if Status[label]['state'] == json_params_config['args'][0]['value']:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario['responseOpen'].format(scenario[value])
            return response_sentence, True
        else:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario.get("response")[0].format(scenario[value])
            return response_sentence, False        
    elif label == '方向盘加热场景':
        if Status[label]['state'] == json_params_config['args'][0]['value']:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario['responseOpen'].format(scenario[value])
            return response_sentence, True
        else:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario.get("response")[0].format(scenario[value])
            return response_sentence, False         
    elif label == '空气净化器场景':
        if Status[label]['state'] == json_params_config['args'][0]['value']:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario['responseOpen'].format(scenario[value])
            return response_sentence, True
        else:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario.get("response")[0].format(scenario[value])
            return response_sentence, False       
    elif label == '雨刷场景':
        if Status[label]['state'] == json_params_config['args'][0]['value']:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario['responseOpen'].format(scenario[value])
            return response_sentence, True
        else:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario.get("response")[0].format(scenario[value])
            return response_sentence, False      
    elif label == '车外灯场景':
        if name == 'setHighBeamStatus':
            statusvalue = Status[label]['lowbeam_state']
        elif name == 'setLowBeamStatus':
            statusvalue = Status[label]['highbeam_state']
        elif name == 'setPositionLampStatus':
            statusvalue = Status[label]['positionlamp_state']
        else:
            statusvalue = 0xff

        if statusvalue == json_params_config['args'][0]['value']:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario['responseOpen'].format(scenario[name],scenario[value])
            return response_sentence, True
        else:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario.get("response")[0].format(scenario[name],scenario[value])
            return response_sentence, False         
    elif label == '空调控制场景':
        if name == 'setSeatHeatVentilationAdj': # '座椅通风加热调节',
            statusvalue = Status[label]['heat_ventilation_state']
        elif name == 'setACTempControl': # '温度控制',
            statusvalue = Status[label]['ac_temp_state']
        elif name == 'setSeatAutoMode': # '座椅自动模式',
            statusvalue = Status[label]['seat_automode_state']
        elif name == 'setClimFanSpeed': # '座椅通风',
            statusvalue = Status[label]['fan_speed_state']
        elif name == 'setClimLeftVentDirection': # '左侧出风口方向',
            statusvalue = Status[label]['left_ventdirection_state']
        elif name == 'setClimRightVentDirection': # '右侧出风口方向', 
            statusvalue = Status[label]['right_ventdirection_state']
        elif name == 'setClimatSyncMode': # '同步模式',
            statusvalue = Status[label]['sync_mode_state']
        elif name == 'setACModeControl': # '空调开关',
            statusvalue = Status[label]['ac_mode_state']
        elif name == 'setInCirculationMode': #'内外循环',
            statusvalue = Status[label]['incirculation_mode_state']
        elif name == 'setClimEVHeaterMode': #'制热模式',
            statusvalue = Status[label]['ev_heater_mode_state']
        elif name == 'setClimAutoNormalMode': #'自动调温'
            statusvalue = Status[label]['autonormal_mode_state']
        else:
            statusvalue = 0xff

        if statusvalue == json_params_config['args'][0]['value']:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario['responseOpen'].format(scenario[name],scenario[value])
            return response_sentence, True
        else:
            value = json_params_config.get("args")[0]["value"]
            response_sentence = scenario.get("response")[0].format(scenario[name],scenario[value])
            return response_sentence, False                         
    else: # 导航场景，
        value = ''
        if len(json_params_list) == 3:
            value = json_params_config.get("args")[0]["value"]
        else:
            value = json_params_config.get("args")[1]["value"]
        response_sentence = scenario.get("response")[0].format(scenario[value])
        return response_sentence, False
    

def extract_identifier_content(text):
    # 正则表达式匹配两个井号之间的内容
    pattern = re.compile(r"#\s*(.*?)\s*#")
    match = pattern.search(text)
    if match:
        return match.group(1)
    else:
        return None


