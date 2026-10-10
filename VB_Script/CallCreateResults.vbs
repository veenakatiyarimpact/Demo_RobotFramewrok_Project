Dim objShell
Set objShell = Wscript.CreateObject("WScript.Shell")

objShell.Run "C:\HSL_Automation\VB_Script\CreateTestResults.vbs" 

' Using Set is mandatory
Set objShell = Nothing