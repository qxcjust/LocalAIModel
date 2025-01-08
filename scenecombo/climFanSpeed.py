from prompts.prompts import *

setclimatefanspeed = {
    "prompts": climate_fanspeed,
    "response": [
        "好的，空调风速已经设置为{}档",
        "了解，空调风速已经设置为{}档"
    ],
    "0x01": "一",
    "0x02": "二",
    "0x03": "三",   
    "0x04": "四", 
    "0x05": "五", 
    "0x06": "六", 
    "0x07": "七"
}


closeclimatefanspeed = {
    "prompts": close_fanspeed,
    "response": [
        "好的，风扇已{}",
        "了解，风扇已{}"
    ],
    "0x00": "关闭"
}