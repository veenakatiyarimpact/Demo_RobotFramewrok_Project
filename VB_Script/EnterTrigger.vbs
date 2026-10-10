Dim objShell
Set objShell = Wscript.CreateObject("WScript.Shell")

objShell.Run "C:\HSL_Automation\VB_Script\Enter_Key.vbs" 

' Using Set is mandatory
Set objShell = Nothing
