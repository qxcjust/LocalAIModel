from prompts.prompts import *

externalLight = {
    "prompts": externalLight_prompt,
    "response": [
        "好的，{}已{}",
    ],

    "0x01": "打开",
    "0x00": "关闭",

    'setHighBeamStatus': '远光灯',
    'setLowBeamStatus': '近光灯',
    'setPositionLampStatus': '位置灯',
    'responseOpen': "{}已经{}",
}