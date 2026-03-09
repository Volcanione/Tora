## GUI 设置

## 初始化
init -2 python:
    gui.init(1280, 720)
    # 强制全局默认字体，防止方块出现
    style.default.font = "fonts/AaFengKuangYuanShiRen-2.ttf"

## 颜色 - 采用更现代、柔和的配色方案
define gui.accent_color = '#ff6b6b'        # 强调色：柔和的红色
define gui.idle_color = '#7f8c8d'          # 空闲色：灰青色
define gui.idle_small_color = '#95a5a6'    # 小文本空闲色
define gui.hover_color = '#ff8787'         # 悬停色：浅红色
define gui.selected_color = '#ffffff'      # 选中色：纯白
define gui.insensitive_color = '#bdc3c77f' # 禁用色
define gui.muted_color = '#2c3e50'         # 暗色背景
define gui.hover_muted_color = '#34495e'   # 暗色背景悬停
define gui.text_color = '#2c3e50'          # 对话文本颜色：深灰蓝（更易读）
define gui.interface_text_color = '#404040' # 界面文本颜色

## 字体
## 强制使用 fonts 目录下的思源黑体解决中文方框问题
define gui.text_font = "fonts/AaFengKuangYuanShiRen-2.ttf"
define gui.interface_text_font = "fonts/AaFengKuangYuanShiRen-2.ttf"
define gui.button_text_font = "fonts/AaFengKuangYuanShiRen-2.ttf"
define gui.choice_button_text_font = "fonts/AaFengKuangYuanShiRen-2.ttf"
define gui.label_font = "fonts/AaFengKuangYuanShiRen-2.ttf"
define gui.headline_font = "fonts/AaFengKuangYuanShiRen-2.ttf"
define gui.name_text_font = "fonts/AaFengKuangYuanShiRen-2.ttf"

## 对话框 - 优化布局与间距
define gui.textbox_height = 210            # 增加高度，更显大气
define gui.textbox_yalign = 1.0
define gui.name_xpos = 300                 # 调整姓名位置
define gui.name_ypos = -10                 # 姓名框稍微上移
define gui.name_width = 200
define gui.name_xalign = 0.0
define gui.dialogue_xpos = 320             # 增加左边距，使文本居中感更强
define gui.dialogue_ypos = 60
define gui.dialogue_width = 640            # 缩小宽度，增加行间距感
define gui.dialogue_xalign = 0.0

## 主菜单布局 (Main Menu)
define gui.navigation_xpos = 80                      # 菜单按钮靠左
define gui.navigation_spacing = 15                   # 按钮间距
define gui.navigation_ypos = 400                     # 菜单按钮垂直位置
define gui.main_menu_background = Solid("#2c3e50")   # 默认主界面背景
define gui.game_menu_background = Solid("#2c3e50")   # 默认游戏菜单背景

## 文本样式
define gui.text_size = 30                  # 增大字号，提升阅读体验
define gui.name_text_size = 36             # 姓名大一号
