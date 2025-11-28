"""
图像翻译SDK使用示例
"""

import cv2
import os
from image_translation_sdk import ImageTranslationSDK
from config import SDKConfig, load_config, save_config

def basic_usage():
    """基本使用示例"""
    print("=== 基本使用示例 ===")
    
    # 1. 创建SDK实例（使用默认配置）
    sdk = ImageTranslationSDK()
    
    # 2. 翻译单张图片
    image_path = "example_images/chinese_image.jpg"  # 替换为实际图片路径
    
    if os.path.exists(image_path):
        try:
            translated_image, info = sdk.translate_image(image_path)
            
            # 保存结果
            cv2.imwrite("translated_result.jpg", translated_image)
            print("✅ 翻译完成！")
            print(f"📄 检测到的文本: {info['detected_texts']}")
            print(f"🌐 翻译结果: {info['translated_texts']}")
            
        except Exception as e:
            print(f"❌ 翻译过程中出错: {e}")
    else:
        print(f"⚠️  示例图片不存在: {image_path}")

def custom_config_usage():
    """自定义配置使用示例"""
    print("\n=== 自定义配置使用示例 ===")
    
    # 1. 创建自定义配置
    custom_config = SDKConfig(
        ocr=OCRConfig(
            model_name="cnocr",
            confidence_threshold=0.8,
            gpu_enabled=True
        ),
        inpainting=InpaintingConfig(
            model_name="lama",
            device="cuda"  # 使用GPU加速
        ),
        translation=TranslationConfig(
            target_language="en",
            service="google"
        ),
        rendering=RenderingConfig(
            font_family="Arial",
            min_font_size=12,
            max_font_size=36
        )
    )
    
    # 2. 使用自定义配置创建SDK
    sdk = ImageTranslationSDK(device='cuda', inpainter_model='lama')
    
    print("✅ 自定义配置SDK创建成功")

def batch_processing_example():
    """批量处理示例"""
    print("\n=== 批量处理示例 ===")
    
    sdk = ImageTranslationSDK()
    
    # 图片文件夹路径
    image_folder = "batch_images"
    
    if os.path.exists(image_folder):
        image_files = [f for f in os.listdir(image_folder) 
                      if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        print(f"📁 发现 {len(image_files)} 张图片需要处理")
        
        for i, image_file in enumerate(image_files, 1):
            image_path = os.path.join(image_folder, image_file)
            
            try:
                translated_image, info = sdk.translate_image(image_path)
                
                # 保存结果
                output_path = f"output_{image_file}"
                cv2.imwrite(output_path, translated_image)
                print(f"✅ [{i}/{len(image_files)}] {image_file} 处理完成")
                
            except Exception as e:
                print(f"❌ [{i}/{len(image_files)}] {image_file} 处理失败: {e}")
    else:
        print(f"⚠️  图片文件夹不存在: {image_folder}")

def config_management_example():
    """配置管理示例"""
    print("\n=== 配置管理示例 ===")
    
    # 1. 加载配置
    config = load_config("my_config.json")
    print("✅ 配置加载成功")
    
    # 2. 修改配置
    config.translation.target_language = "ja"  # 改为日语
    config.rendering.font_family = "MS Gothic"  # 日语字体
    
    # 3. 保存配置
    save_config(config, "my_config.json")
    print("✅ 配置保存成功")

def advanced_features():
    """高级功能示例"""
    print("\n=== 高级功能示例 ===")
    
    sdk = ImageTranslationSDK()
    
    # 1. 只进行文本检测
    image_path = "example_images/chinese_image.jpg"
    if os.path.exists(image_path):
        annotated_image, text_positions = sdk.text_detector.detect_text_positions(image_path)
        cv2.imwrite("detected_text.jpg", annotated_image)
        print("✅ 文本检测完成")
        print(f"📊 检测到 {len(text_positions)} 个文本区域")
    
    # 2. 自定义翻译服务（需要实现具体的翻译接口）
    def custom_translator(texts, target_lang):
        # 这里可以实现自定义翻译逻辑
        return [f"[Custom] {text}" for text in texts]
    
    # 替换SDK的翻译方法
    sdk._translate_texts = custom_translator
    print("✅ 自定义翻译服务已设置")

def performance_tips():
    """性能优化提示"""
    print("\n=== 性能优化提示 ===")
    
    tips = [
        "💡 使用GPU加速: 设置 device='cuda'",
        "💡 批量处理: 使用批处理模式提高效率", 
        "💡 缓存机制: 启用缓存避免重复计算",
        "💡 模型优化: 使用ONNX格式的模型提高推理速度",
        "💡 分辨率调整: 对大图片进行适当缩放",
        "💡 并行处理: 多线程处理多张图片"
    ]
    
    for tip in tips:
        print(tip)

if __name__ == "__main__":
    print("🚀 图像翻译SDK使用示例")
    print("=" * 50)
    
    # 运行各个示例
    basic_usage()
    custom_config_usage()
    batch_processing_example()
    config_management_example()
    advanced_features()
    performance_tips()
    
    print("\n" + "=" * 50)
    print("🎉 所有示例演示完成！")
    print("\n📚 更多功能请参考文档和源代码")