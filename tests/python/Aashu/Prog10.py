first = 0
second = 1
n = 10

print (first)
print(second)

for i in range(3, n+1):
    next = first + second
    first = second
    second = next
    print(next)