
## 基础游戏菜单框架
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    # 导航菜单 (左侧)
    vbox:
        xpos gui.navigation_xpos
        ypos gui.navigation_ypos
        spacing gui.navigation_spacing

        textbutton _("Start Game") action Start():
            text_size 26
            text_idle_color "#7f8c8d"
            text_hover_color "#ff8787"
            text_selected_color "#ffffff"
        textbutton _("Load Game") action ShowMenu("load"):
            text_size 26
            text_idle_color "#7f8c8d"
            text_hover_color "#ff8787"
            text_selected_color "#ffffff"
        if not main_menu:
            textbutton _("Save Game") action ShowMenu("save"):
                text_size 26
                text_idle_color "#7f8c8d"
                text_hover_color "#ff8787"
                text_selected_color "#ffffff"
        textbutton _("Preferences") action ShowMenu("preferences"):
            text_size 26
            text_idle_color "#7f8c8d"
            text_hover_color "#ff8787"
            text_selected_color "#ffffff"
        textbutton _("About") action ShowMenu("about"):
            text_size 26
            text_idle_color "#7f8c8d"
            text_hover_color "#ff8787"
            text_selected_color "#ffffff"

        if main_menu:
            textbutton _("Quit") action Quit(confirm=not main_menu):
                text_size 26
                text_idle_color "#7f8c8d"
                text_hover_color "#ff8787"
                text_selected_color "#ffffff"
        else:
            textbutton _("Main Menu") action MainMenu():
                text_size 26
                text_idle_color "#7f8c8d"
                text_hover_color "#ff8787"
                text_selected_color "#ffffff"
            textbutton _("Return") action Return():
                text_size 26
                text_idle_color "#7f8c8d"
                text_hover_color "#ff8787"
                text_selected_color "#ffffff"

    # 内容区域 (右侧)
    # 使用 fixed 作为主容器，确保子组件可以使用 align 和 pos
    fixed:
        xpos 450
        ypos 50
        xsize 800
        ysize 650
        
        label title:
            text_size 36
            text_color "#ff6b6b"
            ypos 0

        # 将 transclude 放在一个容器中并向下偏移，避免与标题重叠
        vbox:
            ypos 80
            transclude

    textbutton _("Return"):
        xalign 0.95
        yalign 0.95
        text_size 26
        text_idle_color "#7f8c8d"
        text_hover_color "#ff8787"
        action Return()

## 设置界面
screen preferences():
    tag menu
    use game_menu(_("Preferences")):
        vbox:
            spacing 25
            
            # 语言选择
            vbox:
                label _("Language"):
                    text_size 24
                    text_color "#ff6b6b"
                    text_bold True
                hbox:
                    spacing 30
                    # 动态生成语言切换按钮
                    for lang in available_languages:
                        $ lang_name = lang if lang else "English"
                        # 如果是中文文件夹名，可以映射显示名称，或者直接显示文件夹名
                        $ display_name = "中文" if lang == "chinese" else lang_name
                        
                        textbutton display_name action [Language(lang), SetField(persistent, "lang", lang)]:
                            text_size 22
                            text_idle_color "#7f8c8d"
                            text_hover_color "#ff8787"
                            text_selected_color "#ffffff"
            
            # 显示模式
            vbox:
                label _("Display"):
                    text_size 24
                    text_color "#ff6b6b"
                    text_bold True
                hbox:
                    spacing 30
                    textbutton _("Window") action Preference("display", "window"):
                        text_size 22
                        text_idle_color "#7f8c8d"
                        text_hover_color "#ff8787"
                        text_selected_color "#ffffff"
                    textbutton _("Fullscreen") action Preference("display", "fullscreen"):
                        text_size 22
                        text_idle_color "#7f8c8d"
                        text_hover_color "#ff8787"
                        text_selected_color "#ffffff"
            
            # 文字速度
            vbox:
                label _("Text Speed"):
                    text_size 24
                    text_color "#ff6b6b"
                    text_bold True
                bar value Preference("text speed"):
                    style "slider_bar"
                    range 200
            
            # 音量设置
            vbox:
                label _("Music Volume"):
                    text_size 24
                    text_color "#ff6b6b"
                    text_bold True
                bar value Preference("music volume"):
                    style "slider_bar"
            
            vbox:
                label _("Sound Volume"):
                    text_size 24
                    text_color "#ff6b6b"
                    text_bold True
                bar value Preference("sound volume"):
                    style "slider_bar"

## 存档/读档基础界面
screen file_slots(title):
    tag menu
    use game_menu(title):
        # 存档网格
        grid 3 2:
            spacing 20
            
            for i in range(1, 7):
                button:
                    action FileAction(i)
                    xsize 250
                    ysize 200
                    background Solid("#2c3e50")
                    hover_background Solid("#34495e")

                    vbox:
                        align (0.5, 0.5)
                        spacing 10
                        
                        # 缩略图
                        # 使用固定尺寸的容器包裹截图
                        fixed:
                            xsize 200
                            ysize 113
                            xalign 0.5
                            add FileScreenshot(i):
                                xsize 200
                                ysize 113
                        
                        # 存档信息
                        text FileTime(i, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("Empty Slot")):
                            style "slot_name_text"
                            xalign 0.5

screen save():
    tag menu
    use file_slots(_("Save Game"))

screen load():
    tag menu
    use file_slots(_("Load Game"))

style slot_name_text:
    size 18
    color "#ecf0f1"
    idle_color "#bdc3c7"
    hover_color "#ffffff"
    selected_color "#ffffff"

screen about():
    tag menu
    use game_menu(_("About")):
        label _("About Screen Placeholder"):
            text_size 22
            text_color "#ffffff"

## 样式定义
style slider_label:
    size 24
    color "#ff6b6b"
    bold True
    bottom_margin 5

# 修复进度条不可见的问题
style bar:
    ysize 20
    left_bar Solid("#ff6b6b")
    right_bar Solid("#34495e")

style slider_bar is bar:
    xsize 400

style navigation_button_text:
    size 26
    idle_color "#7f8c8d"
    hover_color "#ff8787"
    selected_color "#ffffff"

style check_button_text:
    size 22
    idle_color "#7f8c8d"
    hover_color "#ff8787"
    selected_color "#ffffff"
