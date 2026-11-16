file = open("./././testdata/mylist.txt","r")
file1 = open("./././testdata/newFile.txt","w")

lines = file.readlines()
for line in lines:
    if 'a' not in line:
        file1.write(line)

file.close()
file1.close()