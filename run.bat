@echo off
rem Скрипт запуска эмулятора: run.bat --vfs <путь> [--script <путь>]
cd /d "%~dp0"
python src\emulator.py %*
