# 游戏主入口文件 (基准脚本)

# 移除 python early，改用 init -1
init -1 python:
    import os
    
    # 自动扫描 tl 文件夹获取可用语言列表
    # 默认包含 English (None)
    available_languages = [None]
    tl_path = os.path.join(config.gamedir, "tl")
    
    if os.path.exists(tl_path):
        for d in os.listdir(tl_path):
            # 排除 english 文件夹，因为 English 已经作为 None (默认语言) 存在
            if os.path.isdir(os.path.join(tl_path, d)) and d.lower() != "english":
                available_languages.append(d)

    if persistent.lang is not None:
        # 在初始化阶段设置默认语言
        config.language = persistent.lang

# 定义角色 (使用 ID 作为 Key)
define e = Character("Eileen")

# 游戏开始
label start:
    scene bg room
    show eileen happy
    
    "welcome_msg"
    
    jump chapter1_start

label end_game:
    "game_over_msg"
    return
