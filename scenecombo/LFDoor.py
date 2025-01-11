from prompts.prompts import *

lfdoor = {
    "prompts": left_door,
    "response": [
        "好的，为您{}主驾驶门，注意后方来车哟",
        "了解，为您{}主驾驶门，请注意过往行人"
    ],
    "0x01": "打开",
    "0x02": "关闭",
    "responseOpen": "主驾车门已经打开"
}

rfdoor = {
    "prompts": right_door,
    "response": [
        "好的，为您{}副驾车门，注意后方来车哟",
        "了解，为您{}副驾车门，请注意过往行人"
    ],
    "0x01": "打开",
    "0x02": "关闭",
    "responseOpen": "副驾车门已经打开"
}

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