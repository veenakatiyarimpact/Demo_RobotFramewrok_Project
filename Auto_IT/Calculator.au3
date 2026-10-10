Run("Calc.exe")
WinWaitActive("Calculator")
WinActive("Calculator")
Sleeper()
ControlClick("Calculator", "", "Button5", "Left") ;Click the number 1
Sleeper()
ControlClick("Calculator", "", "Button11", "Left") ;Click the number 2
Sleeper()
ControlClick("Calculator", "", "Button23", "Left") ;Click the + button
Sleeper()
ControlClick("Calculator", "", "Button16", "Left") ;Click the number 3
Sleeper()
ControlClick("Calculator", "", "Button28", "Left") ;Click the Equal button
Sleeper()
WinClose("Calculator")

Func Sleeper()
Sleep(1000)
EndFunc