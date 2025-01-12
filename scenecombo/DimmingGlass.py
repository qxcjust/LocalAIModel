from prompts.prompts import *

front_dimmingglass = {
    "prompts": frontdimmingglass,
    "response": [
        "好的，正在为您将前排调光玻璃{}",
        "了解，正在为您将前排调光玻璃{}"
    ],
    "0x0b": "调暗",
    "0x1b": "调亮"
}

rear_dimmingglass = {
    "prompts": reardimmingglass,
    "response": [
        "好的，正在为您将后排调光玻璃{}",
        "了解，正在为您将后排调光玻璃{}"
    ],
    "0x0b": "调暗",
    "0x1b": "调亮"
}

dimmingglass_obj = {
    "prompts": dimmingglass_prompt,
    "response": [
        "好的，正在为您{}{}",
        "了解，正在为您{}{}"
    ],
    'responseOpen': "您{}已经{}到最大",
    "0x0b": "调暗",
    "0x1b": "调亮",
    "GlassID": {
        '0x00': "前排调光玻璃",
        '0x01': "后排调光玻璃"
    }

}