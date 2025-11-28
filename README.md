# Image Translation SDK

基于 comic-translate 的图像翻译 SDK 工具包

## 项目简介

这是一个独立的图像翻译 SDK，从 comic-translate 项目中提取出来，提供了完整的图像文本检测、识别和翻译功能。

## 安装方式

### 方式一：使用 pip 安装（推荐）

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 安装 SDK
pip install -e .
```

### 方式二：直接使用

```bash
# 安装依赖
pip install -r requirements.txt

# 直接运行示例
python example_usage.py
```

## 项目结构

```
image-translation-sdk/
├── image_translation_sdk.py  # 主要 SDK 代码
├── config.py                 # 配置文件
├── example_usage.py          # 使用示例
├── requirements.txt          # 依赖列表
├── setup.py                  # 安装配置
├── README.md                 # 项目说明
├── README_SDK.md            # SDK 详细文档
└── sdk_venv/                # 资源文件
    ├── chinese_cht_dict.txt
    ├── en_dict.txt
    ├── label_cn.txt
    ├── ppocr_keys_v1.txt
    └── *.yaml               # YOLO 配置文件
```

## 快速开始

```python
from image_translation_sdk import ImageTranslationSDK

# 初始化 SDK
sdk = ImageTranslationSDK()

# 翻译图像
result = sdk.translate_image("input.jpg", "output.jpg", target_lang="zh")
print(f"翻译完成: {result}")
```

## 功能特性

- 🔍 文本检测和识别
- 🌐 多语言翻译支持
- 🖼️ 图像处理和渲染
- ⚙️ 灵活的配置选项
- 📦 独立部署支持

## 依赖说明

主要依赖包括：
- OpenCV (图像处理)
- NumPy (数值计算)
- Pillow (图像操作)
- ONNX Runtime (模型推理)
- PyTorch (深度学习)
- CNOCR (中文OCR)
- GoogleTrans (翻译服务)

## 许可证

本项目基于原 comic-translate 项目的许可证。