from setuptools import setup, find_packages

setup(
    name="image-translation-sdk",
    version="1.0.0",
    description="基于comic-translate的图生图翻译SDK工具",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.21.0",
        "Pillow>=9.0.0",
        "imkit>=0.1.0",
        "onnxruntime>=1.10.0",
        "torch>=1.9.0",
        # OCR相关依赖
        "cnocr>=2.2.2",
        # 翻译服务依赖
        "googletrans>=4.0.0",
        "requests>=2.25.0",
    ],
    extras_require={
        "gpu": [
            "torch>=1.9.0+cu111",
            "onnxruntime-gpu>=1.10.0",
        ],
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)