@echo off
setlocal
cd /d "%~dp0"
".venv\Scripts\python.exe" -m streamlit run dashboard\app.py --server.address 127.0.0.1
