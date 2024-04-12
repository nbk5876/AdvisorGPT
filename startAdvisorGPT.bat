@echo off
REM ============================================
REM startAdvisorGPT.bat
REM Launch the advisor from a desktop icon
REM ============================================
cd "C:\Users\gb105\OneDrive\go\home\Github\Advisor"
call .\venv\Scripts\activate
python gui.py
REM pause