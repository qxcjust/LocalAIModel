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
    wiper = f"val://Vehicle/static/LSWiperWasherCtrl/setFrontWiperMode/{name}"
    externalLight = f"val://Vehicle/static/LSExteriorLightCtrl/{name}"
    climEVheatermode = f"val://Vehicle/static/LSClimateCtrl/setClimEVHeaterMode/{name}"
    circulationMode = f"val://Vehicle/static/LSClimateCtrl/setInCirculationMode/{name}"
    climFanSpeed = f"val://Vehicle/static/LSClimateCtrl/setClimFanSpeed/{name}"
    ACTempControl = f"val://Vehicle/static/LSClimateCtrl/setACTempControl/{name}"
    ACAutoTemp = f"val://Vehicle/static/LSClimateCtrl/{name}"
    chairctrl = f"val://Vehicle/static/LSSeatCtrl/{name}"
    
    name = ""
    if label == "车窗场景":
        name = windowctrl
    elif label == '车门场景':
        name = doorctrl
    elif label == "座椅场景":
        name = chairctrl
    elif label == "后视镜场景":
        name = mirrorctrl
    elif label == '氛围灯场景':
        name = ambientctrl
    elif label == '空气净化器场景':
        name = climatecleaness
    elif label == '方向盘加热场景':
        name = heatedsteeringwheelmode
    elif label == '调光玻璃场景':
        name = DimmingGlass
    elif label == '播放音乐场景':
        name = music
    elif label == '导航场景':
        name = navigation
    elif label == '雨刷场景':
        name = wiper
    elif label == '车外灯场景':
        name = externalLight
    elif label == '空调控制场景':
        name = acmodectrl

    rz_action_template_lf_window = {
        'name': name,
        'args': args
    }
    return rz_action_template_lf_window