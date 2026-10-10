#include <MsgBoxConstants.au3>

Sleeper()
ControlClick("[CLASS:Shell_TrayWnd]", "", "Button1", "Left") ;Click the Disconnect

ControlClick("[CLASS:NotifyIconOverflowWindow]", "", "ToolbarWindow321", "Right") ;Click the Disconnect
Sleeper()
Send("{Left}")
Send("{Left}")


Sleeper()

Func Sleeper()
Sleep(2000)
EndFunc