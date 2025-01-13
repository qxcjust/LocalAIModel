from prompts.prompts import *

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