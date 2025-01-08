from prompts.prompts import *

ambientlight = {
    "prompts": right_window_scene,
    "response": [
        "好的，为您{}副驾车窗",
        "好的，为您{}右前车窗",
        "了解， 我已帮您{}右侧的车窗"
    ],
    'responsefuzzy': [
        "已经为您自动执行打开右前的车窗{}"
    ],
    "0x01": "打开",
    "0x15": "关闭"
}