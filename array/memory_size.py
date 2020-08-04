from array import *
num=array("i",[12,32,45,31])
print(str(num.itemsize))
print(str(num.buffer_info()))
print(str(num.buffer_info()[1]*num.itemsize))