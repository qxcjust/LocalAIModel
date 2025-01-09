from scenecombo.LFWindow import *
from scenecombo.LFDoor import *
from scenecombo.mirror import *
from scenecombo.chair import *
from scenecombo.DimmingGlass import *
from scenecombo.massage import *
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
from scenecombo.lowbeam import *
from scenecombo.highbeam import *
from scenecombo.positionbeam import *
from scenecombo.climAutoNormalMode import *
from scenecombo.climEVheatermode import *

scenario_config_all = {
    '主驾车窗': front_lef_window,
    '副驾车窗': front_right_window,
    '左后车窗': rear_left_window,
    '右后车窗': rear_right_window,
    '所有车窗': allwindow,       
    '主驾座椅': lfchair,
    '副驾座椅': rlchair,
    '主驾车门': lfdoor,
    '副驾车门': lfdoor,
    '左侧后视镜': left_mirror,
    '右侧后视镜': right_mirror,
    '前排调光玻璃': front_dimmingglass,
    '后排调光玻璃': rear_dimmingglass,
    '主驾座椅按摩': left_massage,
    '副驾座椅按摩': right_massage, 
    '主驾座椅通风模式': left_ventilation,
    '副驾座椅通风模式': right_ventilation,     
    '主驾座椅加热模式': left_seatheat,
    '副驾座椅加热模式': right_seatheat,  
    '关闭主驾座椅加热模式': close_left_seatheat,
    '关闭副驾座椅加热模式': close_right_seatheat,    
    '主驾空调温度': left_actempcontrol, 
    '副驾空调温度': right_actempcontrol,
    '播放音乐': play_music,
    '停止播放音乐': stop_music,
    '设置空调风速': setclimatefanspeed,
    '关闭空调风扇': closeclimatefanspeed,
    '主驾座椅自动通风加热': left_Seatautomode,
    '副驾座椅自动通风加热': right_Seatautomode,
    '氛围灯': ambientlight,
    '空气净化器': climatcleaness,
    '同步模式': climatsyncmode,
    '空调控制': acmodectrl,
    '方向盘加热': heatedsteeringwheelmode,    
    '模糊场景': FuzzyInstruction,
    '主驾出风口': climleftventdirection,
    '副驾出风口': climrightventdirection,
    '空气循环模式': climcirculationmode,
    '打开导航': navigation,
    '雨刷设置': frontwipermode,
    '远光灯': highbeam,
    '近光灯': lowbeam,
    '位置灯': positionlamp,
    '空调制热模式': climEVheatermode,
    '自动调温模式': climAutoNormalMode
}

