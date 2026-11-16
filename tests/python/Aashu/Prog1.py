file = open("./././testdata/mylist.txt","r")

lines = file.readlines()
for line in lines:
    words = line.split()
    for word in words:
        print(word+"#",end="")