from prompts.prompts import *

front_lef_window = {
    "prompts": front_left_window_scene,
    "response": [
        "好的，为您{}主驾车窗",
        "好的，为您{}左前车窗",
        "了解， 我已帮您{}左侧的车窗"
    ],
    'responsefuzzy': [
        "已经为您自动执行打开左侧的车窗{}"
    ],
    "0x01": "打开",
    "0x15": "关闭"
}

front_right_window = {
    "prompts": front_right_window_scene,
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

rear_left_window = {
    "prompts": rear_left_window_scene,
    "response": [
        "好的，为您{}左后车窗",
        "了解， 我已帮您{}左后的车窗"
    ],
    'responsefuzzy': [
        "已经为您自动执行打开左后的车窗{}"
    ],
    "0x01": "打开",
    "0x15": "关闭"
}

rear_right_window = {
    "prompts": rear_right_window_scene,
    "response": [
        "好的，为您{}右后车窗",
        "了解， 我已帮您{}右侧的车窗"
    ],
    'responsefuzzy': [
        "已经为您自动执行打开右后的车窗{}"
    ],
    "0x01": "打开",
    "0x15": "关闭"
}

allwindow = {
    "prompts": all_window_scene,
    "response": [
        "好的，为您{}全部车窗",
        "了解， 我已帮您{}全部车窗"
    ],
    'responsefuzzy': [
        "已经为您自动执行打开全部的车窗{}"
    ],
    "0x01": "打开",
    "0x15": "关闭"
}

window_scene_obj = {
    "prompts": window_scene,
    "response": [
        "好的，为您{}{}",
        "了解， 我已帮您{}{}"
    ],
    "0x01": "打开",
    "0x15": "关闭",
    "responseOpen": '{}已经为您打开',
    "WindowAreaID": {
        "0x01": "主驾车窗",
        "0x02": "副驾车窗",
        "0x03": "左后车窗",
        "0x04": "右后车窗",
        "0x05": "全部车窗"
    }    
}