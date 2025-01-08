left_window_scene = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

请帮我打开左侧车窗
返回: setWindowPosition, WindowAreaID, 0x01, WindowPosition, 0x01

请帮我打开主驾车窗
返回: setWindowPosition, WindowAreaID, 0x01, WindowPosition, 0x01

关闭主驾驶车窗
返回: setWindowPosition, WindowAreaID, 0x01, WindowPosition, 0x15

请帮我打开左前车窗
返回: setWindowPosition, WindowAreaID, 0x01, WindowPosition, 0x01
"""

left_back_window_scene = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

请帮我打开左后车窗
返回: setWindowPosition, WindowAreaID, 0x03, WindowPosition, 0x01

请帮我关闭左后车窗
返回: setWindowPosition, WindowAreaID, 0x03, WindowPosition, 0x15
"""

right_window_scene = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

请帮我打开右侧车窗
返回: setWindowPosition, WindowAreaID, 0x02, WindowPosition, 0x01

请帮我打开副驾车窗
返回: setWindowPosition, WindowAreaID, 0x02, WindowPosition, 0x01

关闭副驾驶车窗
返回: setWindowPosition, WindowAreaID, 0x02, WindowPosition, 0x15

请帮我打开右前车窗
返回: setWindowPosition, WindowAreaID, 0x02, WindowPosition, 0x01
"""

right_back_window_scene = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

请帮我打开右后车窗
返回: setWindowPosition, WindowAreaID, 0x04, WindowPosition, 0x01

请帮我关闭右后车窗
返回: setWindowPosition, WindowAreaID, 0x04, WindowPosition, 0x15
"""

all_window_scene = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

请帮我打开全部车窗
返回: setWindowPosition, WindowAreaID, 0x05, WindowPosition, 0x01

请帮我关闭全部车窗
返回: setWindowPosition, WindowAreaID, 0x05, WindowPosition, 0x15
"""

left_door = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

请帮我打开车门
返回: setLockState, DoorID, 0x01, LockState, 0x01

请帮我关闭车门
返回: setLockState, DoorID, 0x01, LockState, 0x02

请帮我打开主驾车门
返回: setLockState, DoorID, 0x01, LockState, 0x01

请帮我关闭主驾车门
返回: setLockState, DoorID, 0x01, LockState, 0x02

请帮我打开左车门
返回: setLockState, DoorID, 0x01, LockState, 0x01

请帮我关闭左车门
返回: setLockState, DoorID, 0x01, LockState, 0x02
"""

right_door = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

请帮我副驾车门
返回: setLockState, DoorID, 0x02, LockState, 0x01

请帮我副驾车门
返回: setLockState, DoorID, 0x02, LockState, 0x02
"""

left_front_mirror = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

请帮我展开左后视镜
返回: setMirrorFoldStaus, MirrorID, 0x01, MirrorFoldStaus, 0x01

请帮我折叠左后视镜
返回: setMirrorFoldStaus, MirrorID, 0x01, MirrorFoldStaus, 0x02
"""

right_front_mirror = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

请帮我展开右后视镜
返回: setMirrorFoldStaus, MirrorID, 0x02, MirrorFoldStaus, 0x01

请帮我折叠右后视镜
返回: setMirrorFoldStaus, MirrorID, 0x02, MirrorFoldStaus, 0x02
"""

left_front_chair = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

主驾座椅往前调节
返回: setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x01

主驾座椅往后调节
返回: setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x02

主驾座椅往上调节
返回: setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x03

主驾座椅往下调节
返回: setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x04

主驾座椅靠背往前调节
返回: setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x05

主驾座椅靠背往后调节
返回: setSeatForwardBackAdj, SeatID, 0x01, Direction, 0x06
"""

right_front_chair = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

副驾座椅往前调节
返回: setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x01

副驾座椅往后调节
返回: setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x02

副驾座椅往上调节
返回: setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x03

副驾座椅往下调节
返回: setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x04

副驾座椅靠背往前调节
返回: setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x05

副驾座椅靠背往后调节
返回: setSeatForwardBackAdj, SeatID, 0x02, Direction, 0x06
"""

frontdimmingglass = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

前排调光玻璃调暗
返回: setDimmingGlassStatus, GlassID, 0x00, DimmingStatus, 0x0b

前排调光玻璃调亮
返回: setDimmingGlassStatus, GlassID, 0x00, DimmingStatus, 0x1b
"""


reardimmingglass = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

后排调光玻璃调暗
返回: setDimmingGlassStatus, GlassID, 0x01, DimmingStatus, 0x0b

后排调光玻璃调亮
返回: setDimmingGlassStatus, GlassID, 0x01, DimmingStatus, 0x1b
"""

flmassage = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

打开主驾座椅按摩
返回: setSeatMassageMode, SeatID, 0x01, MassageMode, 0x01

关闭主驾座椅按摩
返回: setSeatMassageMode, SeatID, 0x01, MassageMode, 0x00
"""


frmassage = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

打开副驾座椅按摩
返回: setSeatMassageMode, SeatID, 0x02, MassageMode, 0x01

关闭副驾座椅按摩
返回: setSeatMassageMode, SeatID, 0x02, MassageMode, 0x00
"""

flVentilation = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置主驾座椅通风模式3档
返回: setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x07

设置主驾座椅通风模式2档
返回: setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x06

设置主驾座椅通风模式1档
返回: setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x05

关闭主驾座椅通风
返回: setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x00
"""


frVentilation = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置副驾座椅通风模式3档
返回: setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x07

设置副驾座椅通风模式2档
返回: setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x06

设置副驾座椅通风模式1档
返回: setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x05

关闭副驾座椅通风
返回: setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x00
"""

flSeatHeat = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置主驾座椅加热模式3档
返回: setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x04

设置主驾座椅加热模式2档
返回: setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x03

设置主驾座椅加热模式1档
返回: setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x02

关闭主驾座椅加热
返回: setSeatHeatVentilationAdj, SeatID, 0x01, HeatVentilationLevel, 0x01
"""


frSeatHeat = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置副驾座椅加热模式3档
返回: setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x04

设置副驾座椅加热模式2档
返回: setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x03

设置副驾座椅加热模式1档
返回: setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x02

关闭副驾座椅加热
返回: setSeatHeatVentilationAdj, SeatID, 0x02, HeatVentilationLevel, 0x01
"""

ambientlight = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

关闭氛围灯

"""


flACTempControl = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置设置主驾空调温度21度
返回: setACTempControl, AreaID, 0x01, Temp, 21

设置设置主驾空调温度22度
返回: setACTempControl, AreaID, 0x01, Temp, 22

设置设置主驾空调温度23度
返回: setACTempControl, AreaID, 0x01, Temp, 23

设置设置主驾空调温度24度
返回: setACTempControl, AreaID, 0x01, Temp, 24

设置设置主驾空调温度25度
返回: setACTempControl, AreaID, 0x01, Temp, 25

设置设置主驾空调温度26度
返回: setACTempControl, AreaID, 0x01, Temp, 26

设置设置主驾空调温度27度
返回: setACTempControl, AreaID, 0x01, Temp, 27

设置设置主驾空调温度28度
返回: setACTempControl, AreaID, 0x01, Temp, 28

设置设置主驾空调温度29度
返回: setACTempControl, AreaID, 0x01, Temp, 29

设置设置主驾空调温度30度
返回: setACTempControl, AreaID, 0x01, Temp, 30

设置设置主驾空调温度31度
返回: setACTempControl, AreaID, 0x01, Temp, 31

设置设置主驾空调温度32度
返回: setACTempControl, AreaID, 0x01, Temp, 32
"""

frACTempControl = """
请你将用户指令{instruction}提取关键信息, 并且返回关键参数。
不要任何额外内容

举例：
用户指令{instruction}: 

设置设置副驾空调温度21度
返回: setACTempControl, AreaID, 0x02, Temp, 21

设置设置副驾空调温度22度
返回: setACTempControl, AreaID, 0x02, Temp, 22

设置设置副驾空调温度23度
返回: setACTempControl, AreaID, 0x02, Temp, 23

设置设置副驾空调温度24度
返回: setACTempControl, AreaID, 0x02, Temp, 24

设置设置副驾空调温度25度
返回: setACTempControl, AreaID, 0x02, Temp, 25

设置设置副驾空调温度26度
返回: setACTempControl, AreaID, 0x02, Temp, 26

设置设置副驾空调温度27度
返回: setACTempControl, AreaID, 0x02, Temp, 27

设置设置副驾空调温度28度
返回: setACTempControl, AreaID, 0x02, Temp, 28

设置设置副驾空调温度29度
返回: setACTempControl, AreaID, 0x02, Temp, 29

设置设置副驾空调温度30度
返回: setACTempControl, AreaID, 0x02, Temp, 30

设置设置副驾空调温度31度
返回: setACTempControl, AreaID, 0x02, Temp, 31

设置设置副驾空调温度32度
返回: setACTempControl, AreaID, 0x02, Temp, 32
"""

fuzzy_instruction_prompt = """
请你将用户的模糊指令{instruction}给予下面场景中最合适的的场景反馈
不要任何额外内容

举例：
模糊指令{instruction}：

我很热
返回: 打开左车窗一半
"""

select_scene_prompt = """
你的任务是做文本分类，将用户指令{instruction}分发到对应的场景上，返回场景名称。
不要任何额外内容

所有场景：
1. 左前车窗
2. 左后车窗
3. 右前车窗
4. 右后车窗
5. 所有车窗      
6. 主驾座椅
7. 副驾座椅
8. 主驾车门
9. 副驾车门
10. 左侧后视镜
11. 右侧后视镜
12. 前排调光玻璃
13. 后排调光玻璃
14. 主驾座椅按摩
15. 副驾座椅按摩
16. 主驾座椅通风模式
17. 副驾座椅通风模式   
18. 主驾座椅加热模式
19. 副驾座椅加热模式
20. 氛围灯
21. 主驾空调温度
22. 副驾空调温度

举例：
用户指令{instruction}：

打开主驾车窗
返回： 左前车窗

关闭左驾车窗
返回： 左前车窗

打开主驾驶座椅按摩
返回： 主驾座椅按摩

关闭前排调光玻璃
返回： 前排调光玻璃

设置副驾座椅通风模式3档
返回： 副驾座椅通风模式

打开副驾座椅按摩
返回： 副驾座椅按摩

打开副驾座椅加热模式3档
返回： 副驾座椅加热

设置主驾空调温度22度
返回： 主驾空调温度
"""