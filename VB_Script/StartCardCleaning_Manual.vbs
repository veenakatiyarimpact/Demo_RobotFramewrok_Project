
   Dim fso
  
   
   Set fso = CreateObject("Scripting.FileSystemObject")
  
   Do 
   If fso.FileExists("\\10.83.20.166\c$\Card Writer\StatusCompleted.txt") Then
       MsgBox "Card Cleaning Started"
      fso.DeleteFile ("\\10.83.20.166\c$\Card Writer\StatusCompleted.txt")
      Exit Do
   End If    
   Loop	

   






Do 
If fso.FileExists("\\10.83.20.166\c$\Card Writer\StatusCompleted.txt") Then
      set fso =Nothing
      MsgBox "Card Cleaning Completed"
      Exit Do
End If    
Loop





