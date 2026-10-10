#include <MsgBoxConstants.au3>
Run("C:\Program Files (x86)\Cisco Systems\VPN Client\vpngui.exe")
WinWaitActive("[CLASS:QWidget]")
WinActive("[CLASS:QWidget]")
Sleeper()
ControlClick("[CLASS:QWidget]", "", "QWidget84", "Left") ;Click the Disconnect
Sleeper()
Send ("{Esc}")
WinClose("[CLASS:QWidget]")
Sleeper()
ControlClick("status: Disconnected | VPN Client - Version 5.0.07.0290", "", "QWidget71", "Left")
Sleeper()
Send ("{Esc}")
Sleeper()
Send("!{F4}")

Func Sleeper()
Sleep(5000)
EndFunc