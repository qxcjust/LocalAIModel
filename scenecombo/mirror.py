from prompts.prompts import *

mirror_obj = {
    "prompts": mirror_prompt,
    "response": [
        "好的，为您{}{}",
        "了解，为您{}{}"
    ],
    'responseOpen': "您{}已经{}",
    "0x01": "展开",
    "0x02": "折叠",
    "MirrorID": {
        '0x01': "左后视镜",'0x02': "右后视镜"
    }
}