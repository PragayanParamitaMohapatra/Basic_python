import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]
print(li1)

# using copy for shallow copy
li2 = copy.copy( li1 )
print(li2)
li2.append(4)
print(li2)

# using deepcopy for deepcopy
li3 = copy.deepcopy( li1 )
print(li3)
li3.append([4,6])
print(li3)
print(li1)