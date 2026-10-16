# Find the first non-repeating character.

name = "Veena Katiyar"

for char in name:
    if name.count(char) == 1:
        print(char)
        break;