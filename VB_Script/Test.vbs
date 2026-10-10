Dim FSO
Set FSO = CreateObject("Scripting.FileSystemObject")

If  fso.FileExists("C:\Automation\B.txt")=false Then
    Msgbox "No"
End If