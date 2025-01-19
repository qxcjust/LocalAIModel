# 默认都是开启状态
Status = {
    '车门场景': {
        'state': '0x01'
    }, 
    '车窗场景': {
        'state': '0x02'
    },
    '座椅场景': {
        'state': '0x01'
    },
    '后视镜场景': {
        'state': '0x01'
    },
    '调光玻璃场景': {
        'state': '0x01'
    },
    '氛围灯场景': {
        'state': '0x01'
    },
    '播放音乐场景': {
        'state': '0x01'
    },
    '方向盘加热场景':{
        'state': '0x01'
    },
    '空气净化器场景':{
        'state': '0x01'
    },
    '雨刷场景':{
        'state': '0x01'
    },    
    '车外灯场景':{
        'lowbeam_state': '0x01',
        'highbeam_state': '0x01',
        'positionlamp_state': '0x01'
    },    
    '空调控制场景':{
        # 测试用
        'heat_ventilation_state': '0xff',
        'ac_temp_state': '0x1a',
        'seat_automode_state': '0xff',
        'fan_speed_state': '0xff',
        'left_ventdirection_state': '0xff',
        'right_ventdirection_state': '0xff',
        'sync_mode_state':'0xff',
        'ac_mode_state':'0xff',
        'incirculation_mode_state':'0xff',
        'ev_heater_mode_state':'0xff',
        'autonormal_mode_state':'0xff',
    }
    # '空调控制场景':{
    #     # TODO 这里其实应该判断所有已经启动的档位
    #     # 'heat_ventilation_state': '0x01',
    #     'heat_ventilation_state': '0xff',
    #     'ac_temp_state': '0x1a',
    #     'seat_automode_state': '0x01',
    #     # TODO 这里其实应该判断所有已经启动的档位
    #     # 'fan_speed_state': '0x01', 
    #     'fan_speed_state': '0xff',
    #     'left_ventdirection_state': '0x01',
    #     'right_ventdirection_state': '0x01',
    #     'sync_mode_state':'0x01',
    #     'ac_mode_state':'0x01',
    #     'incirculation_mode_state':'0x01',
    #     'ev_heater_mode_state':'0x01',
    #     'autonormal_mode_state':'0x01',
    # }
}
