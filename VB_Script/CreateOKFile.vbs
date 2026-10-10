Set objFSO = CreateObject("Scripting.FileSystemObject")
'objFSO.MoveFile "C:\temp\cashregister\LijMaksu.DAT" , "C:\temp\cashregister\LijMaksu.OK"

outFile="C:\temp\cashregister\LijMaksu.OK"
Set objFile = objFSO.CreateTextFile(outFile,True)
objFile.Write "test string" & vbCrLf
objFile.Close

set objFSO =Nothing