Dim objShell
Set objShell = Wscript.CreateObject("WScript.Shell")

objShell.Run "C:\HSL_Automation\Auto_IT\VPNConnect.exe" 
WScript.Sleep (20000)
' Using Set is mandatory
Set objShell = Nothing
