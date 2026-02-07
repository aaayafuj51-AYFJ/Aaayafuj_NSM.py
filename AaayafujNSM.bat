@echo off
title Aaayafuj_NSM Security Suite
setlocal

:: Check for Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed or not in PATH.
    echo [*] Please install Python 3.x to run this tool.
    pause
    exit /b
)

echo [*] Starting Aaayafuj_NSM CLI...
python Aaayafuj_NSM.py

if %errorlevel% neq 0 (
    echo.
    echo [!] Application exited with an error.
    pause
)
