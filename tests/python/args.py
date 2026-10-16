def addition(*args):
    result = 0;

    for num in args:
            result += num

    return result

print(addition(1,2,3))
print(addition(10,20,30,40,50))