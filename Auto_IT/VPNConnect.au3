#include <MsgBoxConstants.au3>

Run("C:\Program Files (x86)\Cisco Systems\VPN Client\vpngui.exe")
WinWaitActive("[CLASS:QWidget]")
WinActive("[CLASS:QWidget]")
Sleeper()
Sleeper()
Run("C:\Program Files (x86)\RSA SecurID Software Token\SecurID.exe")
WinWaitActive("000226707496 - RSA SecurID Token")
WinActive("000226707496 - RSA SecurID Token")
Send("1577")
Send("{ENTER}")
SleeperLess()
Send("{TAB}")
Send("{ENTER}")
SleeperLess()
Local $sData = ClipGet()
SleeperLess()
Send("{ALT}{F4}")
Run("TASKKILL /F /IM SecurID.exe")
SleeperLess()
ControlClick("[CLASS:QWidget]", "", "QWidget84", "Left") ;Click the Connect
SleeperLess()
WinWaitActive("[CLASS:QWidget]")
WinActive("[CLASS:QWidget]")
Send("+{TAB}")
Send("{HOME}+{END}{DEL}")
Send("bapauchi")
Send("{TAB}")
Send($sData)
Send("{TAB}")
Send("{ENTER}")
Sleeper()


Func Sleeper()
Sleep(5000)
EndFunc

Func SleeperLess()
Sleep(1000)
EndFunc