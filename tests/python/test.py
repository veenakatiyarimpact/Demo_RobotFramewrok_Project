# Reverse the text string

name = "Pune International"
revstr = ""

len = len(name)

while (len>0):
	revstr = revstr + (name[len-1])
	len = len-1
	
print(revstr)