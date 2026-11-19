
@echo off

cd /d "%~dp0"

echo =================================
echo       KHOI DONG GAMEZONE
echo =================================

start "" http://127.0.0.1:5500/Bai_tap_lon/TrangChu/index.html

".\..\.venv\Scripts\python.exe" app.py

pause