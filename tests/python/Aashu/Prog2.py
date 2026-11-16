
def countMyChars(filePath):
    
    vowels = 0
    consonants = 0
    lowChars = 0
    upChars = 0

    file = open(filePath,"r")
    content = file.read()
    for char1 in content:
        if char1.isalpha():
            if char1.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
                
        if char1.islower():
            lowChars += 1
        elif char1.isupper():
            upChars += 1

    print("Vowels : ",vowels)
    print("Consonants : ",consonants)
    print("Lowercase Characters : ",lowChars)
    print("Uppercase Characters : ",upChars)

    return vowels, consonants, lowChars, upChars


countMyChars("./././testdata/mylist.txt")