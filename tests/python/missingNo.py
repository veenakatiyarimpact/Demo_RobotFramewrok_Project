
age = [1,2,3,4,5,6,7]

min = min(age)
max = max(age)

for num in range(min,max + 1):
    if(num not in age):
        print(num)