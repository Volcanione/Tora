# Ren'Py 游戏 Demo (Tora)

这是一个基于 Ren'Py 8.3.4 开发的模块化、多语言视觉小说 Demo。

## 📂 目录结构说明

```text
Tora/
├── game/                   # 游戏核心资源目录
│   ├── story/              # [核心] 剧情脚本模块化目录
│   │   ├── chapter1.rpy    # 第一章剧情
│   │   └── chapter2.rpy    # 第二章剧情
│   ├── tl/                 # [核心] 多语言翻译目录
│   │   └── chinese/        # 中文本地化文件夹 (系统自动扫描)
│   │       ├── common.rpy  # 界面翻译 (主菜单、设置、存档等)
│   │       └── story/      # 剧情翻译 (对应 game/story/ 结构)
│   ├── fonts/              # 字体资源 (解决中文乱码)
│   ├── gui/                # 界面图片资源 (背景、按钮、对话框)
│   ├── audio/              # 音频资源 (BGM、SE)
│   ├── images/             # 角色立绘与背景图
│   ├── saves/              # [忽略] 本地存档文件夹
│   ├── script.rpy          # 游戏主入口与初始化逻辑
│   ├── options.rpy         # 游戏全局配置 (名称、版本、窗口)
│   ├── gui.rpy             # GUI 样式与配色定义
│   └── screens.rpy         # 界面 UI 逻辑 (菜单、设置、存档位)
├── fonts/                  # 全局备用字体
├── .gitignore              # Git 忽略规则 (忽略 saves, rpyc 等)
└── README.md               # 项目说明文档
```

## ✨ 核心功能特性

### 1. 动态多语言系统 (i18n)
- **自动扫描加载**：系统启动时自动扫描 `game/tl/` 目录，根据文件夹名称动态生成语言切换按钮。
- **语言持久化**：采用 `init -1 python` 结合 `persistent` 变量，确保玩家选择的语言在重启游戏后依然生效。
- **本地化补全**：主菜单（Start Game/Load Game）及存档界面已完成全中文本地化。

### 2. 模块化剧情维护
- **独立脚本**：剧情按章节存放于 `game/story/`，支持通过 `jump` 指令无缝衔接。
- **结构同步**：翻译文件建议存放在 `game/tl/chinese/story/`，保持与原脚本目录结构一致，方便维护。

### 3. 现代定制化 GUI
- **视觉风格**：采用软色调配色方案（Accent: `#ff6b6b`），优化了对话框、按钮及导航栏样式。
- **存档/读档系统**：重构了 `file_slots` 界面，提供 3x2 网格布局，支持实时截图预览、存档时间戳显示及空位提示。

### 4. 工程化配置
- **Git 友好**：内置 `.gitignore`，自动忽略 `saves/` 文件夹、编译后的 `.rpyc` 文件及系统冗余文件。

## 🛠️ 开发指南

### 增加新章节
1. 在 `game/story/` 下创建新的 `.rpy` 文件（如 `chapter3.rpy`）。
2. 在 `script.rpy` 中使用 `jump chapter3_start` 进行跳转。

### 扩展新语言
1. 在 `game/tl/` 下创建语言文件夹（如 `japanese`）。
2. 在该文件夹内编写翻译脚本（可以使用 Ren'Py SDK 自动生成）。
3. **无需修改代码**：设置菜单会自动识别并显示“japanese”选项。

## 🚀 运行环境
- **Ren'Py SDK**: 8.3.4
- **Python**: 3.9+ (SDK 内置)

## 📝 最近更新记录
- **[2026-03-09] 界面与功能完善**：
  - **UI 增强**：修复了 Preferences 界面配置项消失及文字过大的问题，定义了 `slider_bar` 样式修复进度条不可见。
  - **存档系统**：重构 `file_slots` 界面，增加 `FileScreenshot` 预览和 `FileTime` 时间戳。
  - **多语言持久化**：修复了 `persistent.lang` 导致的 `NoneType` 迭代错误及 `NameError`，确保设置跨会话生效。
  - **本地化补全**：同步更新 `common.rpy`，补全了主菜单、存档界面及占位符的中文翻译。
  - **工程化**：添加 `.gitignore`，采用树状结构优化了 `README.md` 的目录说明。
