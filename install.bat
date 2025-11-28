@echo off
REM Image Translation SDK 安装脚本 (Windows)

echo === Image Translation SDK 安装脚本 ===

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到 Python，请先安装 Python 3.8 或更高版本
    pause
    exit /b 1
)

echo ✓ Python 已安装

REM 创建虚拟环境
echo 正在创建虚拟环境...
python -m venv venv

REM 激活虚拟环境
echo 正在激活虚拟环境...
call venv\Scripts\activate.bat

REM 升级 pip
echo 正在升级 pip...
python -m pip install --upgrade pip

REM 安装依赖
echo 正在安装依赖包...
pip install -r requirements.txt

REM 安装 SDK
echo 正在安装 SDK...
pip install -e .

echo.
echo === 安装完成 ===
echo 要使用 SDK，请运行以下命令激活虚拟环境：
echo venv\Scripts\activate.bat
echo.
echo 然后可以运行示例：
echo python example_usage.py
echo.
echo 或在 Python 中导入使用：
echo from image_translation_sdk import ImageTranslationSDK

pause