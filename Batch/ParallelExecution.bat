SETLOCAL ENABLEDELAYEDEXPANSION

CD C:\Repo\Demo_RobotFramewrok_Project

set myParam=%1
Call pabot --processes %myParam:"=% .\tests