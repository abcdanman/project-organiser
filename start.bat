@echo off
title FYP Project Hub
netstat -an 2>nul | find "8765" | find "LISTEN" >nul 2>&1
if %errorlevel%==0 (
    start "" "http://localhost:8765"
) else (
    start /B python "%~dp0server.py"
    timeout /t 2 /nobreak >nul
    start "" "http://localhost:8765"
)
