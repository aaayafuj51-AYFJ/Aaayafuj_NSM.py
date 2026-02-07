@echo off
title AaayafujNSM CLI Suite
setlocal

:: Check for Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed or not in PATH.
    echo [*] Please install Python 3.x to run this tool.
    pause
    exit /b
)

echo [*] Starting AaayafujNSM CLI...
python AaayafujNSM.py

if %errorlevel% neq 0 (
    echo.
    echo [!] Application exited with an error.
    pause
)
