SETLOCAL ENABLEDELAYEDEXPANSION

CD C:\Repo\UnifiedRobotFramework\Batch
SET "tcs="

FOR %%A IN (%*) DO (
      Set "tcs=!tcs! -t %%A"	  
)

Call pybot %tcs% -T --outputdir C:\Repo\UnifiedRobotFramework\TestResultLogs\Temp C:\Repo\UnifiedRobotFramework\Robot.txt

