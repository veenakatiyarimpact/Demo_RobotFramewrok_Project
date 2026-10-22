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


# //////////////////////////////////

vk = [1,2,3,4,5,[10,20]]
shallow1 = copy.copy(vk)
deep1 = copy.deepcopy(vk)

vk[0] = 6
vk[1] = 7
vk[2] = 8
vk[3] = 9
vk[4] = 10
vk[5][0] = 11
vk[5][1] = 12

print(shallow1)
print(deep1)
