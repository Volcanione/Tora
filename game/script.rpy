# 游戏主入口文件 (基准脚本)

# 显式定义 Live2D 角色，并配置动作映射
# 动作名称 'idle' 对应 mtn/idle.motion3.json
# update_lookat=True 启用鼠标追踪功能
image fred = Live2D("live2d/fred", loop=True, fade=True, default_fade=0.5, update_lookat=True)

# 定义 Fred 角色对象，用于对话
define f = Character("Fred")

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

# 游戏开始
label start:
    python:
        if renpy.has_live2d():
            renpy.say(None, "系统检测：当前环境已成功安装并支持 Live2D。")
        else:
            renpy.say(None, "系统检测：当前环境【不支持】Live2D。请在 Ren'Py 启动器中安装 Live2D Cubism 支持库。")

    scene bg room
    
    # 使用 show 指令显示 Live2D 角色并显式指定播放 idle 动作
    show fred idle:
        xalign 0.5
        yalign 1.0
        zoom 1.0
    
    "welcome_msg"
    
    jump chapter1_start

label end_game:
    "game_over_msg"
    return
