
   Dim fso
   Set fso = CreateObject("Scripting.FileSystemObject")
   Set MyFile=fso.CreateTextFile("\\10.83.12.254\c$\Card Writer\DeviceUnshared.txt",true)
   MyFile.Close() 
   Set MyFile= Nothing 
   Set fso=Nothing
   
    
     
   