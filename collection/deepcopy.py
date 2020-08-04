import copy
li1 = [1, 2, [3,5], 4]
print(id(li1))
li2=copy.deepcopy(li1)
print(li2)
print(id(li2))
li2[2][1]=4
print(li1)
print(li2)
print(id(li2))
print(id(li1))