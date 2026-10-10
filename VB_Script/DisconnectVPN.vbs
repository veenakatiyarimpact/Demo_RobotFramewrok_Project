Dim objShell
Set objShell = Wscript.CreateObject("WScript.Shell")

objShell.Run "C:\HSL_Automation\Auto_IT\VPNDisconnect.exe" 
WScript.Sleep (30000)

' Using Set is mandatory
Set objShell = Nothing
