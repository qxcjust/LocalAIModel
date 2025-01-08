from scenecombo.LFWindow import *
from scenecombo.LFDoor import *
from scenecombo.mirror import *
from scenecombo.chair import *
from scenecombo.DimmingGlass import *
from scenecombo.massage import *
from scenecombo.ventilation import *
from scenecombo.SeatHeat import *

scenario_config = {
    '开左前车窗': lfwindow,
    '关左车门': lfwindow,
    '关左侧车窗': lfwindow,
    '关车门': lfdoor,
    '开车窗': lfwindow,
    '关左后车窗': lfwindow,
    '开左后车窗': lfwindow,
    '关左前车窗': lfwindow,
    '开车门': lfwindow,
    '关右车门': lfdoor,
    '开左侧车窗': lfwindow,
    '停车点2': lfwindow,
    '关闭引擎': lfwindow,
    '关敞篷': lfwindow,
    '关车窗': lfwindow,
    '关右前车窗': lfwindow,
    '停车点1': lfwindow,
    '喇叭': lfwindow,
    '开右前车窗': lfwindow,
    '开右车门': lfdoor,
    '关右后车窗': lfdoor,
    "打开引擎": lfwindow,
    "开右后车窗" : lfdoor,
    "开后备箱": lfwindow,
}

scenario_config_all = {
    '左前车窗': lfwindow,
    '左后车窗': lbwindow,
    '右前车窗': rfwindow,
    '右后车窗': rbwindow,
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
    '副驾座椅加热模式': right_seatheat       
}

