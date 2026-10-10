SETLOCAL ENABLEDELAYEDEXPANSION

CD C:\Repo\UnifiedRobotFramework

set myParam=%1
Call pabot --processes %myParam:"=%
 
 
 
