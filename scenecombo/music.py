from prompts.prompts import *

play_music = {
    "prompts": playmusic,
    "response": [
        "好的，正在为您播放{}",
        "了解，正在为您播放{}"
    ],
    "0x01": "舒缓音乐",
    "0x02": "歌剧音乐",
    "0x03": "钢琴曲",   
    "0x04": "流行音乐", 
    "0x05": "小提琴音乐"
}


stop_music = {
    "prompts": stopmusic,
    "response": [
        "好的，音乐已{}",
        "了解，音乐已{}"
    ],
    
    "0x00": "停止播放",
}