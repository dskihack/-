#  语音内容提取填表系统

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.4-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

一个基于PyQt6的GUI应用程序，用于从语音文件中提取内容并填充到Excel模板中。

## 已实现功能

- 🎤 音频处理功能
  - 支持多种音频格式(WAV, MP3, PCM等)
  - 音频文件分割处理(自动分割为60秒片段)
  - 集成百度语音识别API(支持免费额度)
  - 多音频文件批量处理
  - 语音识别结果显示与基本编辑

- 📊 Excel模板处理
  - 样例Excel模板文件解析
  - 模板表格预览功能
  - 根据模板生成空白表格结构

- 🖥️ 用户界面
  - 分步骤向导式界面设计(4个标签页)
  - 表格数据可视化展示
  - 文件浏览与选择功能
  - 基本的结果导出界面

- 📥 数据导出
  - 结果导出为Excel文件功能

## 待实现功能

- 🤖 智能数据填充核心功能
  - 大模型集成(根据样例、资料和语音文本填充表格)
  - 列名自动匹配与内容填充
  - 多段录音与表格行的对应关系处理
  - 资料Excel与语音文本的关联信息合并

- ✏️ 文本编辑增强
  - 更完善的识别文本编辑与校对功能
  - 多音频识别结果分别编辑
  - 编辑历史记录与撤销功能

- 📈 数据处理增强
  - 资料Excel与语音识别结果的智能合并
  - 数据验证与错误检查
  - 填充规则自定义功能

- 🛠️ 系统增强
  - 更完善的错误处理和用户反馈
  - 处理进度显示与中断功能
  - API调用优化与本地缓存
  - 多语言支持

- 🔍 高级功能
  - 自动保存和恢复工作进度
  - 批量处理模式
  - 自定义音频分割参数
  - 识别结果后处理(标点符号恢复等)

## 截图展示

### 核心界面展示
| ![excel模版](docs/excel模版.png) | ![音频处理](docs/音频处理.png) |
|----------------------------------|--------------------------------|
| ![资料表格](docs/资料表格.png)   | ![结果导出](docs/结果导出.png) |

### 数据处理流程
![解析excel](docs/解析excel.png)
## 安装与使用

### 1. 克隆仓库
首先，将项目克隆到本地：
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. 创建虚拟环境（可选但推荐）
建议使用虚拟环境来运行项目，以避免依赖冲突。以下是使用 `venv` 创建虚拟环境的步骤：

#### 对于 Linux/macOS：
```bash
python3 -m venv myvenv          # 创建虚拟环境
source myvenv/bin/activate      # 激活虚拟环境
```

#### 对于 Windows：
```bash
python -m venv myvenv           # 创建虚拟环境
.\myvenv\Scripts\activate       # 激活虚拟环境
```

### 3. 安装依赖
在激活虚拟环境后，安装项目所需的依赖：
```bash
pip install -r requirements.txt
```

### 4. 运行项目

```bash
python .\ze_frame.py
```

```

