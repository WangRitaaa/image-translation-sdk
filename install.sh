#!/bin/bash

# Image Translation SDK 安装脚本

echo "=== Image Translation SDK 安装脚本 ==="

# 检查 Python 版本
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "错误: 需要 Python 3.8 或更高版本，当前版本: $python_version"
    exit 1
fi

echo "✓ Python 版本检查通过: $python_version"

# 创建虚拟环境
echo "正在创建虚拟环境..."
python3 -m venv venv

# 激活虚拟环境
echo "正在激活虚拟环境..."
source venv/bin/activate

# 升级 pip
echo "正在升级 pip..."
pip install --upgrade pip

# 安装依赖
echo "正在安装依赖包..."
pip install -r requirements.txt

# 安装 SDK
echo "正在安装 SDK..."
pip install -e .

echo ""
echo "=== 安装完成 ==="
echo "要使用 SDK，请运行以下命令激活虚拟环境："
echo "source venv/bin/activate"
echo ""
echo "然后可以运行示例："
echo "python example_usage.py"
echo ""
echo "或在 Python 中导入使用："
echo "from image_translation_sdk import ImageTranslationSDK"