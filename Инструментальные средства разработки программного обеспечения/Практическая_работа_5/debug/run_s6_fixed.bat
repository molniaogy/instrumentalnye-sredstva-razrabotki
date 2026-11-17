@echo off
chcp 65001 >nul
cd /d "%~dp0"
cls
python -X utf8 s6_fixed.py
echo.
pause
