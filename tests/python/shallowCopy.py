import copy

original = [[10, 20], [30, 40]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 1
original[0][1] = 2
original[1][0] = 3
original[1][1] = 4

print(shallow)
print(deep)