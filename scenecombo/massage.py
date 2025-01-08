from prompts.prompts import *

left_massage = {
    "prompts": flmassage,
    "response": [
        "好的，已为您{}主驾座椅按摩",
        "了解，已为您{}主驾座椅按摩"
    ],
    "0x01": "打开",
    "0x00": "关闭"
}

right_massage = {
    "prompts": frmassage,
    "response": [
        "好的，已为您{}副驾座椅按摩",
        "了解，已为您{}副驾座椅按摩"
    ],
    "0x01": "打开",
    "0x00": "关闭"
}