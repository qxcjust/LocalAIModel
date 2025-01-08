from prompts.prompts import *

left_ventilation = {
    "prompts": flVentilation,
    "response": [
        "好的，主驾座椅通风模式已经设置为{}",
        "了解，主驾座椅通风模式已经设置为{}"
    ],
    "0x07": "三档",
    "0x06": "二档",
    "0x05": "一档",   
    "0x00": "关闭" 
}

right_ventilation = {
    "prompts": frVentilation,
    "response": [
        "好的，副驾座椅通风模式已经设置为{}",
        "了解，副驾座椅通风模式已经设置为{}"
    ],
    "0x07": "三档",
    "0x06": "二档",
    "0x05": "一档",   
    "0x00": "关闭" 
}