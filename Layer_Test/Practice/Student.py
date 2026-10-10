from collections import Counter

class Student:
    def __init__(self):
        self.name = "John"
        self._name = "Veena"
        self.__name = "Ashlesha"

s = Student()
print(s.name)
print(s._name)
# print(s.__name) #AttributeError: 'Student' object has no attribute '__name'. Did you mean: '_name'?

class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

p = Child()
p.show()

p = Parent()
p.show()

name = "veena katiyar"
print(name[::-1])


def duplicates(lst):
    print("LIST : " + str(lst))
    seen = list()
    dup = list()

    for item in lst:
        if item in seen:
            dup.append(item)
        else:
            seen.append(item)

    print("Duplicate elements in the list are:", dup) 



duplicates_list = [1, 2, 3, 4, 5, 1, 2, 3]
duplicates(duplicates_list)



text = "python robot pythonx`"

print(Counter(text.split()))

name = "veena Katiyar"
count = Counter(name)

print(count)
print(count.most_common(1))
print(count.most_common(2))
print(count.most_common(3))
print(count.most_common(4))
print(count["a"])
print(count.elements())
print(count.update())
print(count.subtract) 

name = "veena katiyar"

for i in range(len(name)):
    for j in range(i + 1, len(name) + 1):
        print(name[i:j])