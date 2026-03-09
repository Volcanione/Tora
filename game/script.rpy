# 游戏主入口文件 (基准脚本)

# 移除 python early，改用 init -1
init -1 python:
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
