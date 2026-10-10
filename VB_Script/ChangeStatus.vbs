Dim fso, MyFile
	Set fso = CreateObject("Scripting.FileSystemObject")
	Set MyFile = fso.CreateTextFile("\\10.83.12.254\Card Writer\Status.txt", True)
	MyFile.WriteLine("Status=Started")
        MyFile.Close