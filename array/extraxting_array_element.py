from array import *
arr_num=array("i",[1,2,3,4,5])
for i in arr_num:
    if i%2==0:
        print(i)
print("Extract values from index:",end='')
print(arr_num[0],end='&')
print(arr_num[3],end='&')
print(arr_num[4])