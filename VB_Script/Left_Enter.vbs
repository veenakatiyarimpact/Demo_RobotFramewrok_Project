set wsc = CreateObject("WScript.Shell")

WScript.Sleep (500)
wsc.SendKeys ("+{Left}")
WScript.Sleep (500)
wsc.SendKeys ("{Enter}")
