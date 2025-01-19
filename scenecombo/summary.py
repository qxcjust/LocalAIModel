
from scenecombo.LFWindow import *
from scenecombo.LFDoor import *
from scenecombo.mirror import *
from scenecombo.chair import *
from scenecombo.DimmingGlass import *
from scenecombo.music import *
from scenecombo.ambientlight import *
from scenecombo.climatcleaness import *
from scenecombo.FuzzyInstructionScene import *
from scenecombo.heatedsteeringwheelmode import *
from scenecombo.navigation import *
from scenecombo.frontwipermode import *
from scenecombo.externalLight import *
from scenecombo.climate import *

scenario_config_all = {
    '车窗场景': window_scene_obj,
    '座椅场景': chair_obj,
    '车门场景': door_obj,
    '后视镜场景': mirror_obj,
    '调光玻璃场景': dimmingglass_obj,
    '氛围灯场景': ambientlight,
    '播放音乐场景': musicctrl,
    '方向盘加热场景': heatedsteeringwheelmode,   
    '空气净化器场景': climatcleaness,   
    '导航场景': navigation,
    '雨刷场景': frontwipermode,
    '车外灯场景': externalLight,
    '空调控制场景': climate_obj,
    '模糊场景': FuzzyInstruction,
    '5': dimmingglass_obj
}

