@echo off
REM #-----------------------------------------
REM # allcode.bat
REM #-----------------------------------------

REM Define path to allcode.py
set SCRIPT_PATH=C:\Users\gb105\OneDrive\go\home\Github\allcode.py

REM Define input files relative to the current directory
set INPUT_FILES=advise.py,gui.py,files.py,query.py

REM Define the output file path, assuming the current project directory
set OUTPUT_FILE=..\all-code2.txt

REM Call Python script to concatenate files with line numbers
python "%SCRIPT_PATH%" "%INPUT_FILES%" "%OUTPUT_FILE%"