from prompts.prompts import *

chair_obj = {
    "prompts": chair_prompt,
    "response": [
        "好的，为您{}调整{}座椅，注意行驶过程中不要调节",
        "了解，为您{}调整{}座椅，请注意安全",
        "好的，已为您{}{}"
    ],
    # TODO qinxiaocheng修改
    "responseOpen": '经过校验，无法调整座椅暂时',
    "chairadjust": {
        "0x01": "向前",
        "0x02": "向后",
        "0x03": "向上",
        "0x04": "向下",
        "0x05": "靠背向前",
        "0x06": "靠背向后",
        'SeatID': {
            "0x01": '主驾',
            "0x02": '副驾'
        }
    },
    "chairmassage": {
        "0x01": "打开",
        "0x00": "关闭",
        "MassageMode": {
            "0x01": '主驾按摩',
            "0x02": '副驾按摩'
        }
    }
}