age = [10,20,30,10,20,30,40,50,60]
dups = []

for num in age:
    if age.count(num) > 1 and num not in dups:
        dups.append(num)

print( dups)