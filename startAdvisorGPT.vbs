'-------------------------------------------------
'Filename: startAdvisorGPT.vbs
' This VBScript file minimizes the command prompt 
' window when running the Advisor app
'-------------------------------------------------
Set WshShell = CreateObject("WScript.Shell" )
' Run the batch file minimized with focus (window state 6)
WshShell.Run chr(34) & "C:\Users\gb105\OneDrive\go\home\Github\Advisor\startAdvisorGPT.bat" & Chr(34), 6, False
