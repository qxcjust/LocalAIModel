from prompts.prompts import *

lfdoor = {
    "prompts": left_door,
    "response": [
        "好的，为您{}主驾驶门，注意后方来车哟",
        "了解，为您{}主驾驶门，请注意过往行人"
    ],
    "0x01": "打开",
    "0x02": "关闭"
}

rfdoor = {
    "prompts": right_door,
    "response": [
        "好的，为您{}副驾驶门，注意后方来车哟",
        "了解，为您{}副驾驶车门，请注意过往行人"
    ],
    "0x01": "打开",
    "0x02": "关闭"
}