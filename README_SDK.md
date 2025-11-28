# 图像翻译SDK工具

基于comic-translate项目重构的图生图翻译SDK，专注于在不改变图片原有风格、色调、布局、元素相对位置的基础上，进行内容翻译并自动调整图片元素大小以适配翻译后的文字长度。

## 🎯 核心功能

- **智能文本检测**: 使用OCR技术识别图片中的中文文本及其位置
- **高质量图像修复**: 基于LaMa算法移除原始文本，保持图像质量
- **多语言翻译**: 支持中英文等多种语言翻译
- **自适应文本渲染**: 根据原文本区域大小自动调整英文字体
- **批量处理**: 支持多张图片的批量翻译处理

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
# 或使用setup.py安装
pip install -e .
```

### 基本使用

```python
from image_translation_sdk import ImageTranslationSDK

# 创建SDK实例
sdk = ImageTranslationSDK()

# 翻译单张图片
image_path = "your_image.jpg"
translated_image, info = sdk.translate_image(image_path)

# 保存结果
cv2.imwrite("translated_result.jpg", translated_image)

print(f"检测到的文本: {info['detected_texts']}")
print(f"翻译结果: {info['translated_texts']}")
```

## 📁 项目结构

```
comic-translate/
├── image_translation_sdk.py    # SDK核心类
├── config.py                   # 配置文件管理
├── setup.py                    # 安装配置
├── example_usage.py            # 使用示例
└── README_SDK.md              # 本文档
```

## ⚙️ 配置说明

SDK支持灵活的配置选项：

### OCR配置
- `model_name`: OCR模型名称（默认: cnocr）
- `confidence_threshold`: 置信度阈值（默认: 0.7）
- `language`: 识别语言（默认: ch）

### 图像修复配置
- `model_name`: 修复模型（默认: lama）
- `backend`: 推理后端（默认: onnx）
- `device`: 计算设备（auto/cpu/cuda）

### 翻译配置
- `target_language`: 目标语言（默认: en）
- `service`: 翻译服务（google/deepl/gpt）
- `api_key`: API密钥

### 使用自定义配置

```python
from config import SDKConfig, OCRConfig, InpaintingConfig

custom_config = SDKConfig(
    ocr=OCRConfig(confidence_threshold=0.8, gpu_enabled=True),
    inpainting=InpaintingConfig(device="cuda")
)

sdk = ImageTranslationSDK(device='cuda')
```

## 🔧 核心组件

### 1. TextPositionDetector
文本位置检测器，负责识别图片中的中文文本及其位置信息。

```python
detector = TextPositionDetector()
annotated_image, text_positions = detector.detect_text_positions("image.jpg")
```

### 2. ImageTranslationSDK
核心翻译类，整合了文本检测、图像修复、翻译和文本渲染功能。

### 3. 图像修复模块
基于comic-translate的LaMa修复器，提供高质量的图像修复能力。

## 🎨 工作流程

1. **文本检测**: 使用OCR识别图片中的中文文本和位置
2. **文本翻译**: 将识别到的中文翻译成目标语言（如英文）
3. **图像修复**: 使用LaMa算法擦除原始文本区域
4. **文本渲染**: 将翻译后的文本渲染到修复后的图像上
5. **大小适配**: 自动调整字体大小以适应原文本区域

## 📊 性能优化

### GPU加速
```python
sdk = ImageTranslationSDK(device='cuda')
```

### 批量处理
```python
# 批量处理多张图片
image_files = ["img1.jpg", "img2.jpg", "img3.jpg"]
for image_file in image_files:
    result, info = sdk.translate_image(image_file)
```

### 缓存机制
启用缓存避免重复计算，提高处理效率。

## 🔍 高级功能

### 自定义翻译服务
```python
def my_translator(texts, target_lang):
    # 实现自定义翻译逻辑
    return translated_texts

sdk._translate_texts = my_translator
```

### 只进行文本检测
```python
detector = sdk.text_detector
annotated_image, positions = detector.detect_text_positions("image.jpg")
```

## 🐛 故障排除

### 常见问题

1. **图片加载失败**
   - 检查文件路径是否正确
   - 确认图片格式支持（jpg, png等）

2. **文本检测效果不佳**
   - 调整OCR置信度阈值
   - 尝试不同的OCR模型

3. **修复效果不理想**
   - 检查遮罩生成是否正确
   - 调整修复模型参数

### 日志调试
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 扩展开发

### 添加新的OCR模型
继承`TextPositionDetector`类，实现自定义的OCR检测逻辑。

### 集成新的翻译服务
实现自定义的翻译函数，替换SDK中的`_translate_texts`方法。

### 自定义渲染引擎
修改`_render_translated_text`方法，实现个性化的文本渲染效果。

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个SDK！

## 📄 许可证

本项目基于MIT许可证开源。

## 🙏 致谢

感谢comic-translate项目提供的核心图像处理技术。

---

**注意**: 这是一个基于comic-translate重构的SDK工具，保留了原项目的核心功能，同时提供了更简洁的API接口和更好的可扩展性。