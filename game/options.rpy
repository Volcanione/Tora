## 游戏设置

# 启用语言持久化
define config.save_physical_size = True

## 游戏名称
define config.name = _("My Visual Novel")

## 是否在主界面显示游戏名称
define gui.show_name = True

## 主界面背景音乐
# define config.main_menu_music = "audio/main_menu_theme.mp3"

## 多语言配置
## 默认语言设置为英语 (None 在此处代表脚本原始语言)
# 移除这里的硬编码，让 script.rpy 中的 persistent 逻辑生效

## 游戏版本
define config.version = "1.0"

## 存档目录
define config.save_directory = "renpy_demo-12345678"

## 窗口图标
# define config.window_icon = "gui/window_icon.png"

## 默认文本速度 (0 为瞬间显示，建议设置为 50 左右以观察进度条效果)
default preferences.text_cps = 50

## 默认自动前进延迟
default preferences.afm_time = 15

## 转换设置
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

## 窗口模式
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "Tora-1.0"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Tora"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    