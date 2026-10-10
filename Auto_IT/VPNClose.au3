#include <MsgBoxConstants.au3>
WinWaitActive("[CLASS:QWidget]")
WinActive("[CLASS:QWidget]")
Sleeper()
ControlClick("[CLASS:QWidget]", "", "QWidget3", "Left")
Sleeper()
ControlClick("[CLASS:QWidget]", "", "QWidget1", "Left") ;Click the OK
Sleeper()
Send ("{Esc}")
WinClose("[CLASS:QWidget]")


Func Sleeper()
Sleep(1500)
EndFunc