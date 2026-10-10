 

Dim fso,wCount
   Set fso = CreateObject("Scripting.FileSystemObject")
   Set objShell = Wscript.CreateObject("WScript.Shell")
   
   

   Do 
     If fso.FileExists("\\10.83.21.229\c$\Card Writer\StatusCompleted.txt") And fso.FileExists("\\10.83.21.229\c$\Card Writer\DeviceUnshared.txt") Then
        fso.DeleteFile ("\\10.83.21.229\c$\Card Writer\DeviceUnshared.txt")
        objShell.Run "C:\HSL_Automation\Auto_IT\ShareDevice.exe"
        WScript.Sleep(30000)
        set objShell=Nothing
        'MsgBox" Card Cleaning Started"
        fso.DeleteFile ("\\10.83.21.229\c$\Card Writer\StatusCompleted.txt")
        
        Exit Do
     End IF
                WScript.Sleep(1000)      
     
     wCount=wCount+1
     if (wCount>1500) Then
         
         'Msgbox"Long Wait "&Now

         set Myfile1=fso.CreateTextFile("\\10.83.21.229\c$\Card Writer\DeviceUnshared.txt",true)
         set Myfile2=fso.CreateTextFile("\\10.83.21.229\c$\Card Writer\StatusCompleted.txt",true)
         
         MyFile1.Close() 
         MyFile2.Close() 
         
         Set MyFile1= Nothing 
         Set MyFile2= Nothing 
         
         'Msgbox"Long Wait Over"  
        
        
     End If        
   Loop
   
   
                

   



Set objShell = Wscript.CreateObject("WScript.Shell")

Do 
If fso.FileExists("\\10.83.21.229\c$\Card Writer\StatusCompleted.txt") Then
      objShell.Run "C:\HSL_Automation\Auto_IT\UnShareDevice.exe"
      WScript.Sleep(30000)
      Set MyFile=fso.CreateTextFile("\\10.83.21.229\c$\Card Writer\DeviceUnshared.txt",true)
      MyFile.Close() 
      Set MyFile= Nothing 
      Set fso=Nothing
      'MsgBox "Card Cleaning Completed"
      Exit Do
End If    
Loop
