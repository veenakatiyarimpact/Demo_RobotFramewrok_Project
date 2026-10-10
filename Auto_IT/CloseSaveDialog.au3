WinWaitActive("Save As")
WinActive("Save As")
Sleeper()
ControlClick("Save As", "", "Button3", "Left") ;Click the Cancel Button
WinClose("Save As")

Func Sleeper()
Sleep(1000)
EndFunc