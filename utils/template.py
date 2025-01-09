def rz_action_template_lf_window(name: str, args: list, label: str) -> dict:

    print(f"rz_action_template_lf_window === >>>> {label}")

    climatecleaness = f"val://Vehicle/static/LSClimateCtrl/setClimatCleaness/{name}"
    climatsyncmode = f"val://Vehicle/static/LSClimateCtrl/setClimatSyncMode/{name}"
    acmodectrl = f"val://Vehicle/static/LSClimateCtrl/setACModeControl/{name}"
    heatedsteeringwheelmode = f"val://Vehicle/static/LSClimateCtrl/setClimHeatedSteeringWheelMode/{name}"
    ambientctrl = f"val://Vehicle/static/LSAmbientLightCtrl/setAmbientLightColor/{name}"
    DimmingGlass = f"val://Vehicle/static/LSDimmingGlass/setDimmingGlassStatus/{name}"
    windowctrl = f"val://Vehicle/static/LSWindowCtrl/setWindowPosition/{name}"
    doorctrl = f"val://Vehicle/static/LSDoorCtrl/setLockState/{name}"
    mirrorctrl = f"val://Vehicle/static/LSMirrorCtrl/setMirrorFoldStaus/{name}"
    navigation = f"val://Vehicle/static/LauncherService/LauncherNavigation/{name}"
    music = f"val://Vehicle/static/LauncherService/LauncherMusic/{name}"
    massage = f"val://Vehicle/static/LSSeatCtrl/setSeatMassageMode/{name}"
    wiper = f"val://Vehicle/static/LSWiperWasherCtrl/setFrontWiperMode/{name}"
    beam = f"val://Vehicle/static/LSExteriorLightCtrl/{name}"
    climEVheatermode = f"val://Vehicle/static/LSClimateCtrl/setClimEVHeaterMode/{name}"
    circulationMode = f"val://Vehicle/static/LSClimateCtrl/setInCirculationMode/{name}"
    climFanSpeed = f"val://Vehicle/static/LSClimateCtrl/setClimFanSpeed/{name}"
    ACTempControl = f"val://Vehicle/static/LSClimateCtrl/setACTempControl/{name}"
    ACAutoTemp = f"val://Vehicle/static/LSClimateCtrl/{name}"
    chairctrl = f"val://Vehicle/static/LSSeatCtrl/{name}"
    
    name = ""
    if label == "主驾车窗" or label == "副驾车窗" or label == "左后车窗" or label == "右后车窗" or label == "所有车窗":
        name = windowctrl
    elif label == '主驾车门' or label == '副驾车门':
        name = doorctrl
    elif label == "主驾驶座椅" or label == "副驾驶座椅":
        name = doorctrl
    elif label == "左侧后视镜" or label == "右侧后视镜":
        name = mirrorctrl
    elif label == "主驾驶座椅" or label == "副驾驶座椅":
        name = chairctrl
    elif label == '氛围灯':
        name = ambientctrl
    elif label == '空气净化器':
        name = climatecleaness
    elif label == '同步模式':
        name = climatsyncmode
    elif label == '空调控制':
        name = acmodectrl
    elif label == '方向盘加热':
        name = heatedsteeringwheelmode
    elif label == '前排调光玻璃' or label =='后排调光玻璃':
        name = DimmingGlass
    elif label == '打开导航':
        name = navigation
    elif label == '播放音乐' or label == '停止播放音乐':
        name = music
    elif label == '主驾座椅按摩' or label == '副驾座椅按摩':
        name = massage
    elif label == '雨刷设置':
        name = wiper
    elif label == '车外灯':
        name = beam
    elif label == '空调制热模式':
        name = climEVheatermode
    elif label == '空气循环模式':
        name = circulationMode
    elif label == '设置空调风速' or label == '关闭空调风扇':
        name = climFanSpeed   
    elif label == '主驾空调温度' or label == '副驾空调温度':
        name = ACTempControl 
    elif label == '自动调温模式':
        name = ACAutoTemp


    rz_action_template_lf_window = {
        'name': name,
        'args': args
    }
    return rz_action_template_lf_window