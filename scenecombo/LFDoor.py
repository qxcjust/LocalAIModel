from prompts.prompts import *

door_obj = {
    "prompts": door_prompt,
    "response": [
        "好的，为您{}{}车门，注意后方来车哟",
        "了解，为您{}{}车门，请注意过往行人"
    ],
    "0x01": "打开",
    "0x02": "关闭",
    "responseOpen": "{}车门已经打开",
    "DoorID": {
        "0x01": "主驾车门",
        "0x02": "副驾车门"
    }
}