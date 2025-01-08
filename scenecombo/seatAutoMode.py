from prompts.prompts import *

left_Seatautomode = {
    "prompts": flSeatautomode,
    "response": [
        "好的，主驾座椅自动通风加热已{}",
        "了解，主驾座椅自动通风加热已{}"
    ],
    "0x01": "打开",
    "0x00": "关闭"
}

right_Seatautomode = {
    "prompts": frSeatautomode,
    "response": [
        "好的，副驾座椅自动通风加热已{}",
        "了解，副驾座椅自动通风加热已{}"
    ],
    "0x01": "打开",
    "0x00": "关闭"
}