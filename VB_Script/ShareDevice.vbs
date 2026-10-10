Dim objShell
Set objShell = Wscript.CreateObject("WScript.Shell")

objShell.Run "C:\HSL_Automation\Auto_IT\ShareDevice.exe" 

' Using Set is mandatory
Set objShell = Nothing
