#  Find the shortest word in an String

name = "This isd Veena an K"

words = name.split(" ")
minLength = len(name)
minWord = name

for word in words:
    if(len(word) < minLength):
        minLength = len(word)
        minWord = word

print(minLength)
print(minWord)