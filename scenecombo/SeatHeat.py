from prompts.prompts import *

left_seatheat = {
    "prompts": flSeatHeat,
    "response": [
        "好的，主驾座椅加热模式已经设置为{}",
        "了解，主驾座椅加热模式已经设置为{}"
    ],
    "0x04": "三档",
    "0x03": "二档",
    "0x02": "一档",   
    "0x01": "关闭" 
}

right_seatheat = {
    "prompts": frSeatHeat,
    "response": [
        "好的，副驾座椅加热模式已经设置为{}",
        "了解，副驾座椅加热模式已经设置为{}"
    ],
    "0x04": "三档",
    "0x03": "二档",
    "0x02": "一档",   
    "0x01": "关闭" 
}