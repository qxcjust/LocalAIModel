from prompts.prompts import *

left_mirror = {
    "prompts": left_front_mirror,
    "response": [
        "好的，为您{}左后视镜",
        "了解，为您{}左后视镜"
    ],
    "0x01": "展开",
    "0x02": "折叠"
}

right_mirror = {
    "prompts": right_front_mirror,
    "response": [
        "好的，为您{}右后视镜",
        "了解，为您{}右后视镜"
    ],
    "0x01": "展开",
    "0x02": "折叠"
}