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