from scenecombo.LFWindow import *
from scenecombo.LFDoor import *
from scenecombo.mirror import *
from scenecombo.chair import *
from scenecombo.DimmingGlass import *
from scenecombo.ventilation import *
from scenecombo.SeatHeat import *
from scenecombo.ACTempControl import *
from scenecombo.music import *
from scenecombo.climFanSpeed import *
from scenecombo.seatAutoMode import *
from scenecombo.ambientlight import *
from scenecombo.climatcleaness import *
from scenecombo.FuzzyInstructionScene import *
from scenecombo.climatsyncmode import *
from scenecombo.acmodectrl import *
from scenecombo.heatedsteeringwheelmode import *
from scenecombo.ventdirection import *
from scenecombo.circulationmode import *
from scenecombo.navigation import *
from scenecombo.frontwipermode import *
from scenecombo.externalLight import *
from scenecombo.climAutoNormalMode import *
from scenecombo.climEVheatermode import *

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
    '主驾座椅通风模式': left_ventilation,
    '副驾座椅通风模式': right_ventilation,     
    '主驾座椅加热模式': left_seatheat,
    '副驾座椅加热模式': right_seatheat,  
    '关闭主驾座椅加热模式': close_left_seatheat,
    '关闭副驾座椅加热模式': close_right_seatheat,    
    '主驾空调温度': left_actempcontrol, 
    '副驾空调温度': right_actempcontrol,
    '设置空调风速': setclimatefanspeed,
    '主驾座椅自动通风加热': left_Seatautomode,
    '副驾座椅自动通风加热': right_Seatautomode,
    '同步模式': climatsyncmode,
    '空调控制': acmodectrl,
    '主驾出风口': climleftventdirection,
    '副驾出风口': climrightventdirection,
    '空气循环模式': climcirculationmode,
    '空调制热模式': climEVheatermode,
    '自动调温模式': climAutoNormalMode,
    '模糊场景': FuzzyInstruction
}

