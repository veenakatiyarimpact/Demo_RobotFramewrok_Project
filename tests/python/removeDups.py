age = [10,20,30,10,20,30,40,50,0]

age1 = list(set(age))
print(age1)

# ================================================

unique = []
for num in age:
    if num not in unique:
        unique.append(num)


print(unique)