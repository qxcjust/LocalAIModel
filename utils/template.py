def rz_action_template_lf_window(name: str, args: list, label: str) -> dict:
    windowctrl = f"val://Vehicle/static/LSWindowCtrl/{name}"
    doorctrl = f"val://Vehicle/static/LSDoorCtrl/setLockState/{name}"
    mirrorctrl = f"val://Vehicle/static/LSMirrorCtrl/{name}"
    chairctrl = f"val://Vehicle/static/LSSeatCtrl/{name}"

    name = ""
    if label == "左前车窗" or label == "左后车窗" or label == "右前车窗" or label == "右后车窗" or label == "所有车窗":
        name = windowctrl
    elif label == "主驾驶座椅" or label == "副驾驶座椅":
        name = doorctrl
    elif label == "左侧后视镜" or label == "右侧后视镜":
        name = mirrorctrl
    elif label == "主驾驶座椅" or label == "副驾驶座椅":
        name = chairctrl
        
    rz_action_template_lf_window = {
        'name': name,
        'args': args
    }
    return rz_action_template_lf_window