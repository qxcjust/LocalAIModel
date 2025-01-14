from prompts.prompts import *

# climate_prompt = """
# 提取{instruction}空调控制参数,不要任何额外内容。

# 座椅通风/加热:
# SeatID: 0x01(主驾),0x02(副驾)
# HeatVentilationLevel: 
# 通风: 0x07(三档),0x06(二档),0x05(一档),0x00(关闭)
# 加热: 0x04(三档),0x03(二档),0x02(一档),0x01(关闭)

# 温度/风速:
# AreaID: 0x01(主驾),0x02(副驾)
# Temp: 16-32度
# FanSpeed: 0x00(关),0x01-0x07(一到七档)

# 自动通风加热:
# AreaID: 0x01(主驾),0x02(副驾)
# SWStatus: 0x01(开),0x00(关)

# 出风模式:
# 主驾:setClimLeftVentDirection,副驾:setClimRightVentDirection
# FlowDistrMode: 0x04(除霜),0x03(吹脸脚),0x02(吹脸),0x01(吹脚)

# 同步模式控制/打开关闭控制/制热模式控制/自动调温模式控制:
# SWStatus: 0x01(开),0x00(关)
# CycleState: 0x01(内循环),0x02(外循环)

# 示例:
# 主驾通风三档:#setSeatHeatVentilationAdj,SeatID,0x01,HeatVentilationLevel,0x07#
# 主驾温度21度:#setACTempControl,AreaID,0x01,Temp,21#
# 主驾自动通风:#setSeatAutoMode,SeatID,0x01,SWStatus,0x01#
# 主驾吹头:#setClimLeftVentDirection,FlowDistrMode,0x04#
# 开同步模式:#setClimatSyncMode,SWStatus,0x01#
# 开空调:#setACModeControl,SWStatus,0x01#
# 内循环:#setInCirculationMode,CycleState,0x01#
# 开制热模式:#setClimEVHeaterMode,SWStatus,0x01#
# 开自动调温:#setClimAutoNormalMode,SWStatus,0x01#
# """

climate_obj = {
    "prompts": climate_prompt,
    "response": {
        "setSeatHeatVentilationAdj": "好的，已为您将{}座椅调节至{}", ## 通风，加热挡位
        "setACTempControl": "好的，已为您将{}温度调整到{}度", ## 温度
        "setSeatAutoMode": "好的，已为您将{}座椅自动模式{}", ## 主驾 打开 ##########调整座椅要加热还是通风
        "setClimFanSpeed": "好的，已为您将{}座椅通风调节至{}", ## 主驾 通风档位
        "setClimLeftVentDirection": "好的，已为您将主驾{}功能开启", ## 除霜 打开
        "setClimRightVentDirection": "好的，已为您将副驾{}功能开启", ## 除霜 打开
        "setClimatSyncMode": "好的，已为您将同步模式{}", ## 打开
        "setACModeControl": "好的，已为您将空调{}", ## 打开
        "setInCirculationMode": "好的，已为您将空气{}{}", ## 内循环 打开
        "setClimEVHeaterMode": "好的，已为您将制热模式{}", ## 打开
        "setClimAutoNormalMode": "好的，已为您将自动调温{}" ## 打开
    },
    # "response": [
    #     "好的，已为您将温度调整到{}度",
    #     "好的，已为您{}空调",
    #     "好的，已为您将风速调整到{}档", 
    #     "好的，已为您将空调设置为{}模式",
    #     "好的，已为您将{}座椅{}",
    #     "好的，已为您将{}出风口调整为{}",
    #     "好的，已为您将空气循环模式调整为{}"
    # ],
    "responseOpen": '{}已经为您打开',
    "methods": {
        "setSeatHeatVentilationAdj": "座椅通风加热调节",
        "setACTempControl": "温度控制",
        "setSeatAutoMode": "座位自动通风加热",
        "setClimFanSpeed": "座舱通风",
        "setClimLeftVentDirection": "左侧出风口方向",
        "setClimRightVentDirection": "右侧出风口方向", 
        "setClimatSyncMode": "同步模式",
        "setACModeControl": "空调",
        "setInCirculationMode": "内或外循环",
        "setClimEVHeaterMode": "制热模式",
        "setClimAutoNormalMode": "自动调温"
    },
    # "methods": {
    #     "setSeatHeatVentilationAdj": "座椅通风加热调节",
    #     "setACTempControl": "温度控制",

    #     "setSeatAutoMode": "座椅自动模式",
    #     "setClimFanSpeed": "座椅通风",

    #     "setClimLeftVentDirection": "左侧出风口方向",
    #     "setClimRightVentDirection": "右侧出风口方向", 
    #     "setClimatSyncMode": "同步模式",
    #     "setACModeControl": "空调开关",
    #     "setInCirculationMode": "内外循环",
    #     "setClimEVHeaterMode": "制热模式",
    #     "setClimAutoNormalMode": "自动调温"
    # },
    "SeatID": {
        "0x01": "主驾",
        "0x02": "副驾"
    },
    "AreaID": {
        "0x01": "主驾",
        "0x02": "副驾"
    },
    "HeatVentilationLevel": {
        "0x07": "通风三档",
        "0x06": "通风二档",
        "0x05": "通风一档",
        "0x04": "加热三档", 
        "0x03": "加热二档",
        "0x02": "加热一档",
        "0x01": "关闭加热",
        "0x00": "关闭通风"
    },
    "FlowDistrMode": {
        "0x04": "除霜",
        "0x03": "吹脸脚",
        "0x02": "吹脸",
        "0x01": "吹脚"
    },
    "SWStatus": {
        "0x01": "打开",
        "0x00": "关闭"
    },
    "CycleState": {
        "0x01": "内循环",
        "0x02": "外循环"
    },
    "FanSpeed": {
        "0x07": "七档",
        "0x06": "六档",
        "0x05": "五档", 
        "0x04": "四档",
        "0x03": "三档",
        "0x02": "二档",
        "0x01": "一档",
        "0x00": "关闭"
    }
}