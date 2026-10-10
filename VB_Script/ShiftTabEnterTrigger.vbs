Dim objShell
Set objShell = Wscript.CreateObject("WScript.Shell")

objShell.Run "C:\HSL_Automation\VB_Script\Shift_Tab_Enter.vbs" 

' Using Set is mandatory
Set objShell = Nothing
