window_scene = """
请将用户指令{instruction}提取关键信息,返回关键参数。
不要任何额外内容。

关键参数说明:
- WindowAreaID: 0x01(主驾/左前), 0x02(副驾/右前), 0x03(左后), 0x04(右后), 0x05(全部)
- WindowPosition: 0x01(打开), 0x15(关闭)

举例:
用户指令{instruction}:

打开主驾车窗/左前车窗
#setWindowPosition, WindowAreaID, 0x01, WindowPosition, 0x01#

关闭主驾车窗
#setWindowPosition, WindowAreaID, 0x01, WindowPosition, 0x15#

打开副驾车窗/右前车窗
#setWindowPosition, WindowAreaID, 0x02, WindowPosition, 0x01#

关闭副驾车窗
#setWindowPosition, WindowAreaID, 0x02, WindowPosition, 0x15#

打开左后车窗
#setWindowPosition, WindowAreaID, 0x03, WindowPosition, 0x01#

关闭左后车窗
#setWindowPosition, WindowAreaID, 0x03, WindowPosition, 0x15#

打开右后车窗
#setWindowPosition, WindowAreaID, 0x04, WindowPosition, 0x01#

关闭右后车窗
#setWindowPosition, WindowAreaID, 0x04, WindowPosition, 0x15#

打开全部车窗
#setWindowPosition, WindowAreaID, 0x05, WindowPosition, 0x01#

关闭全部车窗
#setWindowPosition, WindowAreaID, 0x05, WindowPosition, 0x15#
"""

door_prompt = """
请将用户指令{instruction}提取关键信息,返回关键参数。
不要任何额外内容。

关键参数说明:
- DoorID: 0x01(主驾), 0x02(副驾)
- LockState: 0x01(打开), 0x02(关闭)

举例:
用户指令{instruction}:

打开主驾车门
#setLockState, DoorID, 0x01, LockState, 0x01#

关闭主驾车门
#setLockState, DoorID, 0x01, LockState, 0x02#

打开副驾车门
#setLockState, DoorID, 0x02, LockState, 0x01#

关闭副驾车门
#setLockState, DoorID, 0x02, LockState, 0x02#
"""

mirror_prompt = """
提取{instruction}中的关键信息,返回关键参数。
不要任何额外内容。

关键参数说明:
- MirrorID: 0x01(左后视镜), 0x02(右后视镜)
- MirrorFoldStaus: 0x01(展开), 0x02(折叠)

示例:
展开左后视镜
#setMirrorFoldStaus, MirrorID, 0x01, MirrorFoldStaus, 0x01#

折叠左后视镜
#setMirrorFoldStaus, MirrorID, 0x01, MirrorFoldStaus, 0x02#

展开右后视镜
#setMirrorFoldStaus, MirrorID, 0x02, MirrorFoldStaus, 0x01#

折叠右后视镜
#setMirrorFoldStaus, MirrorID, 0x02, MirrorFoldStaus, 0x02#
"""

chair_prompt = """
提取{instruction}中的座椅控制参数,返回关键参数。
不要任何额外内容。

参数说明:
- SeatID: 0x01(主驾), 0x02(副驾)
- Direction: 0x01(前), 0x02(后), 0x03(上), 0x04(下), 0x05(靠背前), 0x06(靠背后)
- MassageMode: 0x01(开), 0x00(关)

示例:
主驾座椅往前调节
#setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x01#

主驾座椅往后调节
#setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x02#

主驾座椅往上调节
#setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x03#

主驾座椅往下调节
#setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x04#

主驾座椅靠背往前调节
#setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x05#

主驾座椅靠背往后调节
#setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x06#

副驾座椅往前调节
#setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x01#

副驾座椅往后调节
#setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x02#

副驾座椅往上调节
#setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x03#

副驾座椅往下调节
#setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x04#

副驾座椅靠背往前调节
#setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x05#

副驾座椅靠背往后调节
#setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x06#

打开主驾座椅按摩
#setSeatMassageMode, SeatID, 0x01, MassageMode, 0x01#

关闭主驾座椅按摩
#setSeatMassageMode, SeatID, 0x01, MassageMode, 0x00#

打开副驾座椅按摩
#setSeatMassageMode, SeatID, 0x02, MassageMode, 0x01#

关闭副驾座椅按摩
#setSeatMassageMode, SeatID, 0x02, MassageMode, 0x00#
"""

dimmingglass_prompt = """
提取{instruction}中调光玻璃参数:
GlassID: 0x00(前排), 0x01(后排)
DimmingStatus: 0x0b(调暗), 0x1b(调亮)
不要任何额外内容。

示例:
调暗前排调光玻璃
#setDimmingGlassStatus, GlassID, 0x00, DimmingStatus, 0x0b#

调亮后排调光玻璃 
#setDimmingGlassStatus, GlassID, 0x01, DimmingStatus, 0x1b#
"""

ambientlight_prompts = """
解析用户指令{instruction}并返回氛围灯参数，不要任何额外内容
Color参数对应:
- 0x01: 关闭
- 0x02: 红色
- 0x03: 黄色
- 0x04: 橙色
- 0x05: 蓝色
- 0x0c: 闪烁模式
- 0x0d: 呼吸模式

示例:
关闭氛围灯
#setAmbientLightColor, Color, 0x01#

设置氛围灯颜色为红色
#setAmbientLightColor, Color, 0x02#

设置氛围灯闪烁模式
#setAmbientLightColor, Color, 0x0c#

设置氛围灯呼吸模式
#setAmbientLightColor, Color, 0x0d#
"""

musicctrl_prompt = """
提取{instruction}音乐参数，不要任何额外内容
MusicId: 0x00(停止), 0x01(舒缓), 0x02(歌剧), 0x03(钢琴), 0x04(流行), 0x05(小提琴)
MusicType: 0x01

示例:
停止音乐
#LauncherMusic, MusicId, 0x00, MusicType, 0x01#

播放舒缓音乐
#LauncherMusic, MusicId, 0x01, MusicType, 0x01#
"""

heatedsteeringwheelmode_prompts = """
提取{instruction}方向盘加热参数，不要任何额外内容
SWStatus: 0x01(打开), 0x00(关闭)

示例:
打开方向盘加热
#setClimHeatedSteeringWheelMode, SWStatus, 0x01#

关闭方向盘加热
#setClimHeatedSteeringWheelMode, SWStatus, 0x00#
"""

climatcleaness_prompts = """
提取{instruction}空气净化器参数，不要任何额外内容
CleanMode: 0x01(打开), 0x02(关闭)

示例：
打开PM2.5空气净化器
#setClimatCleaness, CleanMode, 0x02#

关闭PM2.5空气净化器
#setClimatCleaness, CleanMode, 0x01#
"""

navigation_prompt = """
提取{instruction}导航参数，不要任何额外内容

示例：
打开导航
#LauncherNavigation, address, 0x07#
""" 

frontwipermode_prompt = """
提取{instruction}雨刷参数, 不要任何额外内容
FrontWiperMode参数对应:
- 0x00: 关闭
- 0x01: 间歇摆动
- 0x02: 单次摆动
- 0x03: 高速摆动
- 0x04: 低速摆动

示例：
雨刷低速摆动
#setFrontWiperMode, FrontWiperMode, 0x04#

关闭雨刷
#setFrontWiperMode, FrontWiperMode, 0x00#
""" 

externalLight_prompt = """
提取{instruction}车外灯控制参数，不要任何额外内容
- 位置灯: setPositionLampStatus, PositionlampStatus, 0x01(开)/0x00(关)
- 远光灯: setHighBeamStatus, lampStatus, 0x01(开)/0x00(关)  
- 近光灯/小灯: setLowBeamStatus, lampStatus, 0x01(开)/0x00(关)

示例:
打开位置灯
#setPositionLampStatus, PositionlampStatus, 0x01#

关闭远光灯  
#setHighBeamStatus, lampStatus, 0x00#

打开近光灯
#setLowBeamStatus, lampStatus, 0x01#
"""

flVentilation = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

0x07: 三档, 0x06: 二档, 0x05: 一档
设置主驾座椅通风模式三档
#setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x07#

关闭主驾座椅通风
#setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x00#
"""


frVentilation = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

0x07: 三档, 0x06: 二档, 0x05: 一档
设置副驾座椅通风模式三档
#setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x07#

关闭副驾座椅通风
#setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x00#
"""

flSeatHeat = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

0x04: 三档, 0x03: 二档, 0x02:一档
设置主驾座椅加热模式三档
#setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x04#

关闭主驾座椅加热
#setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x01#
"""


closeflSeatHeat = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

关闭主驾座椅加热
#setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x01#
"""


frSeatHeat = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

0x04: 三档, 0x03: 二档, 0x02: 一档
设置副驾座椅加热模式三档
#setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x04#

关闭副驾座椅加热
#setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x01#
"""

closefrSeatHeat = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

关闭副驾座椅加热
#setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x01#
"""

flACTempControl = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置设置主驾空调温度21度
#setACTempControl, AreaID, 0x01, Temp, 21#

设置设置主驾空调温度22度
#setACTempControl, AreaID, 0x01, Temp, 22#

设置设置主驾空调温度32度
#setACTempControl, AreaID, 0x01, Temp, 32#
"""

frACTempControl = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置设置副驾空调温度21度
#setACTempControl, AreaID, 0x02, Temp, 21#

设置设置副驾空调温度22度
#setACTempControl, AreaID, 0x02, Temp, 22#

设置设置副驾空调温度32度
#setACTempControl, AreaID, 0x02, Temp, 32#
"""


climate_fanspeed = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

一档: 0x01, 二档: 0x02, 三档: 0x03, 四档: 0x04, 五档: 0x05, 六档: 0x06, 七档: 0x07
设置空调风速一档
#setClimFanSpeed, AreaID, 0x01, FanSpeed, 0x01#

关闭空调风扇
#setClimFanSpeed, AreaID, 0x01, FanSpeed, 0x00#
"""

flSeatautomode = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

打开主驾座椅自动通风加热
#setSeatAutoMode, SeatID, 0x01, SWStatus, 0x01#

关闭主驾座椅自动通风加热
#setSeatAutoMode, SeatID, 0x01, SWStatus, 0x00#
"""

frSeatautomode = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

打开副驾座椅自动通风加热
#setSeatAutoMode, SeatID, 0x02, SWStatus, 0x01#

关闭副驾座椅自动通风加热
#setSeatAutoMode, SeatID, 0x02, SWStatus, 0x00#
"""

climatsyncmode_prompts = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

接受返回格式：
a,b,c
拒绝返回格式
[a,b,c]

举例：
用户指令{instruction}: 

启动同步模式
#setClimatSyncMode, SWStatus, 0x01#

关闭同步模式
#setClimatSyncMode, SWStatus, 0x00#
""" 


acmodectrl_prompts = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

打开空调
#setACModeControl, SWStatus, 0x01#

关闭空调
#setACModeControl, SWStatus, 0x00#
""" 

climleftventdirection_prompt = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置主驾出风口方向为吹头
#setClimLeftVentDirection, FlowDistrMode, 0x04#

设置主驾出风口方向为吹脸吹脚
#setClimLeftVentDirection, FlowDistrMode, 0x03#

设置主驾出风口方向为吹脸
#setClimLeftVentDirection, FlowDistrMode, 0x02#

设置主驾出风口方向为吹脚
#setClimLeftVentDirection, FlowDistrMode, 0x01#
""" 

climrightventdirection_prompt = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置主驾出风口方向为吹头
#setClimRightVentDirection, FlowDistrMode, 0x04#

设置主驾出风口方向为吹脸吹脚
#setClimRightVentDirection, FlowDistrMode, 0x03#

设置主驾出风口方向为吹脸
#setClimRightVentDirection, FlowDistrMode, 0x02#

设置主驾出风口方向为吹脚 | 设置主驾出风口方向为吹角
#setClimRightVentDirection, FlowDistrMode, 0x01#
""" 

climcirculationmode_prompt = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置空气循环模式为内循环
#setInCirculationMode, CycleState, 0x01#

设置空气循环模式为外循环
#setInCirculationMode, CycleState, 0x02#
""" 

climEVheatermode_prompt = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

打开空调制热模式
#setClimEVHeaterMode, SWStatus, 0x01#

关闭空调制热模式
#setClimEVHeaterMode, SWStatus, 0x00#
""" 

climAutoNormalMode_prompt = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

打开自动调温模式
#setClimAutoNormalMode, SWStatus, 0x01#

关闭自动调温模式
#setClimAutoNormalMode, SWStatus, 0x00#
""" 

fuzzy_instruction_prompt = """
请你将用户的模糊指令{instruction}给予下面场景中最合适的的场景反馈
不要任何额外内容


举例：
模糊指令{instruction}：

我很热
返回: 打开左车窗一半
"""

