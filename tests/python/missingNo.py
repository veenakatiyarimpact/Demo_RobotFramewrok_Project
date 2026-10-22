
age = [1,2,3,4,5,6,7]

min1 = min(age)
max1 = max(age)

for num in range(min1,max1 + 1):
    if(num not in age):
        print(num)