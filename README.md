# Ren'Py 游戏 Demo 项目文档

这是一个基于 Ren'Py 引擎的基础游戏 Demo，旨在展示 Ren'Py 的核心功能（对话、分支、配置和 GUI）。

## 🚀 快速开始

### 1. 环境准备
本项目已为您在 `d:/学习/python/renpy_sdk` 目录下安装了 Ren'Py 8.3.4 SDK。

### 2. 导入项目到 Launcher
如果您想在 Ren'Py Launcher 中看到本项目，请尝试以下任一方法：
- **方法 A (推荐)**: 点击 Launcher 的 **"Preferences" (设置)** -> **"Projects Directory" (项目目录)** -> 选择本项目的父目录 `d:/学习/python/`。
- **方法 B (最快)**: 直接将本项目的 `renpy` 文件夹拖入 Ren'Py Launcher 窗口。

### 3. 运行游戏
在终端中执行以下命令即可启动游戏：
```powershell
pwsh.exe -Command "& 'd:/学习/python/renpy_sdk/renpy-8.3.4-sdk/renpy.exe' 'd:/学习/python/renpy'"
```

### 3. 在 Launcher 中显示项目
如果 Ren'Py Launcher 列表中没有显示本项目：
1. 打开 Ren'Py Launcher，点击 **"Preferences" (设置)**。
2. 点击 **"Projects Directory" (项目目录)**。
3. 选择本项目的**父目录**：`d:/学习/python/`。
4. 返回主界面，即可看到名为 `renpy` 的项目。

## 📂 目录结构说明

```text
renpy/
├── game/                   # 游戏核心资源与脚本目录
│   ├── audio/              # 音频文件 (mp3, ogg, wav)
│   ├── fonts/              # 字体文件 (ttf, otf)
│   ├── gui/                # 界面 UI 图片资源 (按钮、对话框背景等)
│   ├── images/             # 游戏素材 (背景图 bg, 立绘 side/sprite)
│   ├── gui.rpy             # 界面样式与布局定义
│   ├── options.rpy         # 游戏全局配置 (分辨率、版本、存档路径)
│   ├── script.rpy          # 游戏主入口与全局定义
│   └── story/              # 剧情脚本目录
│       ├── chapter1.rpy    # 第一章剧情模块
│       └── chapter2.rpy    # 第二章剧情模块
├── README.md               # 项目说明文档
└── install_renpy.ps1       # SDK 自动化安装脚本
```

## 🛠️ 详细配置指南

### 1. 剧情编写与模块化
- **主入口 (`game/script.rpy`)**: 负责全局变量定义（如角色 `define`）和初始跳转 `jump`。
- **独立章节**: 您可以在 `game/story/` 目录下创建任意数量的 `.rpy` 文件，Ren'Py 会自动递归加载子目录下的脚本。
- **跳转逻辑**: 使用 `jump label_name` 在不同文件间切换剧情。
- **基础语法**:
    - **定义角色**: `define e = Character("艾琳")`
    - **显示背景**: `scene bg room`
    - **显示立绘**: `show eileen happy`
    - **对话分支**: 使用 `menu:` 语句块。

### 2. 资源命名规范
Ren'Py 拥有强大的自动识别机制：
- **背景图**: 命名为 `bg room.jpg`，在脚本中通过 `scene bg room` 调用。
- **角色立绘**: 命名为 `eileen happy.png`，在脚本中通过 `show eileen happy` 调用。
- **音频**: 
    - 背景音乐: `play music "audio/bgm.mp3"`
    - 音效: `play sound "audio/effect.wav"`

### 3. 界面自定义 (`game/gui.rpy`)
- **分辨率**: 在 `gui.init(1280, 720)` 中修改。
- **配色方案**: 已更新为现代柔和配色（强调色 `#ff6b6b`，文本色 `#2c3e50`）。
- **布局优化**: 调整了对话框高度（210px）和文本间距，提升了阅读舒适度。
- **主界面配置**: 在 `options.rpy` 中设置游戏名称，在 `gui.rpy` 中通过 `gui.navigation_xpos` 调整主菜单按钮位置。
- **模块化多语言架构**:
    - 原始脚本 (`game/story/`) 仅包含逻辑 ID。
    - 翻译文件按语言完全隔离在 `game/tl/chinese/` 和 `game/tl/english/` 目录下。
    - 剧情翻译存放在各语言目录下的 `story/` 子目录中，实现了真正的文案与逻辑分离。
- **界面自定义**: 提供了自定义的 `screens.rpy`，允许在设置界面直接切换语言。
- **字体**: 字体文件存放在 `game/fonts/` 目录，通过 `gui.text_font` 等变量引用。

### 4. 游戏设置 (`game/options.rpy`)
- **存档位置**: 修改 `config.save_directory`。
- **转场效果**: 修改 `config.enter_transition` (例如使用 `fade`, `dissolve`)。

## ⌨️ 常用快捷键 (开发模式)

- `Shift + R`: **快速重载**。修改脚本后保存，按此键可立即在游戏中看到效果。
- `Shift + D`: **开发者菜单**。包含变量查看器、跳转标签等。
- `Shift + I`: **样式检查器**。查看 UI 元素的属性。
- `>` (句号): 快速跳过对话。
- `Ctrl` (长按): 强制跳过。
- `F5`: 快速存档。

## 🐞 调试命令

在终端中带调试参数启动：
```powershell
pwsh.exe -Command "& 'd:/学习/python/renpy_sdk/renpy-8.3.4-sdk/renpy.exe' 'd:/学习/python/renpy' --debug"
```

## ⚠️ 常见问题

### 中文乱码/显示方块
- **原因**: 默认字体不支持中文。
- **解决**: 在 `game/gui.rpy` 中设置 `gui.text_font = "AaFengKuangYuanShiRen-2.ttf"`（Ren'Py 内置字体）。
- **编码**: 确保所有 `.rpy` 文件保存为 **UTF-8** 编码。

## 📚 学习资源
- [Ren'Py 官方中文文档](https://www.renpy.cn/doc/)
- [Ren'Py 官方论坛 (Lemma Soft)](https://lemmasoft.renai.us/forums/)
