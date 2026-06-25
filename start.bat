@echo off
title FYP Project Hub
cd /d "%~dp0"
python -c "import pywebview" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing pywebview (first run only)...
    pip install pywebview --quiet
)
pythonw app.py
