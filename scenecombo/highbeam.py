from prompts.prompts import *

highbeam = {
    "prompts": beam_prompt,
    "response": [
        "好的，{}已{}",
    ],

    "0x01": "打开",
    "0x00": "关闭",

    'setHighBeamStatus': '远光灯',
    'setLowBeamStatus': '近光灯',
    'setPositionLampStatus': '位置灯'
}