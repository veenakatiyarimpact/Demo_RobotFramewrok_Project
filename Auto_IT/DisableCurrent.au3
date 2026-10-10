#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.12.0
 Author:         myName

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here
#include <MsgBoxConstants.au3>
Run("TASKKILL /F /IM UsbConfig.exe")
Sleeper()
Run("C:\Program Files\Eltima Software\USB Network Gate\UsbConfig.exe")
Sleeper()
ControlClick("USB Network Gate 6.2 by Eltima Software", "", "Button4", "Left") ;Click on Demo
Sleeper()
ControlClick("USB Network Gate 6.2 by Eltima Software", "", "AfxWnd90su8", "Right") ;Click on Demo

Send ("{DOWN}")
Sleeper()
Send ("{DOWN}")
Sleeper()
Send ("{DOWN}")
Sleeper()
Send("{ENTER}")
Sleeper()
Run("TASKKILL /F /IM UsbConfig.exe")
Sleeper()


Func Sleeper()
Sleep(2000)
EndFunc