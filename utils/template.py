def rz_action_template_lf_window(name: str, args: list, label: str) -> dict:
    windowctrl = f"val://Vehicle/static/LSWindowCtrl/{name}"
    doorctrl = f"val://Vehicle/static/LSDoorCtrl/setLockState/{name}"
    mirrorctrl = f"val://Vehicle/static/LSMirrorCtrl/{name}"
    chairctrl = f"val://Vehicle/static/LSSeatCtrl/{name}"
    ambientctrl = f"val://Vehicle/static/LSAmbientLightCtrl/{name}"
    climatecleaness = f"val://Vehicle/static/LSClimateCtrl/setClimatCleaness/{name}"
    climatsyncmode = f"val://Vehicle/static/LSClimateCtrl/setClimatSyncMode/{name}"
    acmodectrl = f"val://Vehicle/static/LSClimateCtrl/setACModeControl/{name}"
    heatedsteeringwheelmode = f"val://Vehicle/static/LSClimateCtrl/setClimHeatedSteeringWheelMode/{name}"

    name = ""
    if label == "左前车窗" or label == "左后车窗" or label == "右前车窗" or label == "右后车窗" or label == "所有车窗":
        name = windowctrl
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

    rz_action_template_lf_window = {
        'name': name,
        'args': args
    }
    return rz_action_template_lf_window