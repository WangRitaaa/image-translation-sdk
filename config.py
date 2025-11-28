"""
图像翻译SDK配置文件
"""

from dataclasses import dataclass
from typing import Dict, Any, List

@dataclass
class OCRConfig:
    """OCR配置"""
    model_name: str = "cnocr"
    confidence_threshold: float = 0.7
    language: str = "ch"
    gpu_enabled: bool = False

@dataclass
class InpaintingConfig:
    """图像修复配置"""
    model_name: str = "lama"
    backend: str = "onnx"
    device: str = "auto"
    pad_mod: int = 8

@dataclass
class TranslationConfig:
    """翻译配置"""
    target_language: str = "en"
    service: str = "google"  # google, deepl, gpt, etc.
    api_key: str = ""
    timeout: int = 30

@dataclass
class RenderingConfig:
    """文本渲染配置"""
    font_family: str = "Arial"
    min_font_size: int = 10
    max_font_size: int = 40
    text_color: str = "#000000"
    outline_enabled: bool = True
    outline_color: str = "#FFFFFF"
    outline_width: int = 2
    alignment: str = "center"

@dataclass
class SDKConfig:
    """SDK总配置"""
    ocr: OCRConfig = OCRConfig()
    inpainting: InpaintingConfig = InpaintingConfig()
    translation: TranslationConfig = TranslationConfig()
    rendering: RenderingConfig = RenderingConfig()
    
    # 性能配置
    batch_size: int = 1
    cache_enabled: bool = True
    log_level: str = "INFO"
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "ocr": {
                "model_name": self.ocr.model_name,
                "confidence_threshold": self.ocr.confidence_threshold,
                "language": self.ocr.language,
                "gpu_enabled": self.ocr.gpu_enabled,
            },
            "inpainting": {
                "model_name": self.inpainting.model_name,
                "backend": self.inpainting.backend,
                "device": self.inpainting.device,
                "pad_mod": self.inpainting.pad_mod,
            },
            "translation": {
                "target_language": self.translation.target_language,
                "service": self.translation.service,
                "api_key": self.translation.api_key,
                "timeout": self.translation.timeout,
            },
            "rendering": {
                "font_family": self.rendering.font_family,
                "min_font_size": self.rendering.min_font_size,
                "max_font_size": self.rendering.max_font_size,
                "text_color": self.rendering.text_color,
                "outline_enabled": self.rendering.outline_enabled,
                "outline_color": self.rendering.outline_color,
                "outline_width": self.rendering.outline_width,
                "alignment": self.rendering.alignment,
            },
            "performance": {
                "batch_size": self.batch_size,
                "cache_enabled": self.cache_enabled,
                "log_level": self.log_level,
            }
        }
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'SDKConfig':
        """从字典创建配置对象"""
        config = cls()
        
        if "ocr" in config_dict:
            ocr_config = config_dict["ocr"]
            config.ocr = OCRConfig(
                model_name=ocr_config.get("model_name", "cnocr"),
                confidence_threshold=ocr_config.get("confidence_threshold", 0.7),
                language=ocr_config.get("language", "ch"),
                gpu_enabled=ocr_config.get("gpu_enabled", False),
            )
        
        if "inpainting" in config_dict:
            inpaint_config = config_dict["inpainting"]
            config.inpainting = InpaintingConfig(
                model_name=inpaint_config.get("model_name", "lama"),
                backend=inpaint_config.get("backend", "onnx"),
                device=inpaint_config.get("device", "auto"),
                pad_mod=inpaint_config.get("pad_mod", 8),
            )
        
        if "translation" in config_dict:
            trans_config = config_dict["translation"]
            config.translation = TranslationConfig(
                target_language=trans_config.get("target_language", "en"),
                service=trans_config.get("service", "google"),
                api_key=trans_config.get("api_key", ""),
                timeout=trans_config.get("timeout", 30),
            )
        
        if "rendering" in config_dict:
            render_config = config_dict["rendering"]
            config.rendering = RenderingConfig(
                font_family=render_config.get("font_family", "Arial"),
                min_font_size=render_config.get("min_font_size", 10),
                max_font_size=render_config.get("max_font_size", 40),
                text_color=render_config.get("text_color", "#000000"),
                outline_enabled=render_config.get("outline_enabled", True),
                outline_color=render_config.get("outline_color", "#FFFFFF"),
                outline_width=render_config.get("outline_width", 2),
                alignment=render_config.get("alignment", "center"),
            )
        
        if "performance" in config_dict:
            perf_config = config_dict["performance"]
            config.batch_size = perf_config.get("batch_size", 1)
            config.cache_enabled = perf_config.get("cache_enabled", True)
            config.log_level = perf_config.get("log_level", "INFO")
        
        return config


# 默认配置
DEFAULT_CONFIG = SDKConfig()

def load_config(config_path: str = None) -> SDKConfig:
    """从文件加载配置"""
    import json
    import os
    
    if config_path is None:
        # 使用默认配置文件路径
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
    
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config_dict = json.load(f)
        return SDKConfig.from_dict(config_dict)
    else:
        # 如果配置文件不存在，创建默认配置并保存
        save_config(DEFAULT_CONFIG, config_path)
        return DEFAULT_CONFIG

def save_config(config: SDKConfig, config_path: str = None):
    """保存配置到文件"""
    import json
    import os
    
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
    
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config.to_dict(), f, indent=2, ensure_ascii=False)