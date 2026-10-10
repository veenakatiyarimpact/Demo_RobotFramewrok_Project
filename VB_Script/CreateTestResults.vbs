Option Explicit  
Dim fso, path, folder, recentDate, recentFolder,destFolder,strSafeDate,strSafeTime,strDateTime,newfolder,wsc,strUserName 

set wsc = CreateObject("WScript.Shell")

WScript.Sleep (20000)

strUserName = wsc.ExpandEnvironmentStrings( "%USERNAME%" )

set wsc=Nothing



destFolder="C:\HSL_Automation_Regression\TestResults\"

strSafeDate =   Right("0" & DatePart("d",Date), 2)&"."& Right("0" & DatePart("m",Date), 2) &"."& DatePart("yyyy",Date) 
 
strSafeTime = Right("0" & Hour(Now), 2) &"."& Right("0" & Minute(Now), 2) &"."& Right("0" & Second(Now), 2)
 
strDateTime = "TestResults_"&strSafeDate & "_" & strSafeTime




Set fso = CreateObject("Scripting.FileSystemObject")
Set newfolder = fso.CreateFolder(destFolder&strDateTime)
Set recentFolder = Nothing
For Each folder in fso.GetFolder("C:\Users\"&strUserName&"\AppData\Local\Temp").SubFolders
  If (recentFolder is Nothing) Then
    Set recentFolder = folder
  ElseIf ( InStr(1, folder.Name, "RIDE") <> 0) And (folder.DateLastModified > recentFolder.DateLastModified)  Then
    Set recentFolder = folder
  End If
  
Next
fso.CopyFolder recentFolder,destFolder&strDateTime
