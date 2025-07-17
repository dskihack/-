#  语音内容提取填表系统

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.4-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

一个基于PyQt6的GUI应用程序，用于从语音文件中提取内容并填充到Excel模板中。

## 功能特点

- 🎤 支持多种音频格式(WAV, MP3等)
- 📊 Excel模板解析与预览
- ✏️ 识别文本编辑功能
- 📥 结果导出为Excel文件
- 🖥️ 用户友好的界面设计

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
（如果你的项目没有 `requirements.txt`，你可以手动列出依赖，比如 `pip install flask numpy pandas`）

### 4. 运行项目
根据你的项目，运行主程序或启动服务。例如：
```bash
python main.py
```
或
```bash
flask run
```

### 5. 退出虚拟环境（可选）
完成后，可以退出虚拟环境：
```bash
deactivate
```

---
