from collections import Counter


name = "Veena Katiyar"
frequency = {}


for char in name:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char in frequency:
    print(char , " : " , frequency[char])

# ======================================

print(Counter(name));


# ======================================

print(Counter([10,20,30,10,20,30,40,50,0,60]))


