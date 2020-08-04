n=int(input("enter size:"))
a={}
val_arr=[]
for i in range(0,n):
    name=input("Enter std name:")
    mark=float(input("Enter marks:"))
    a[name]=mark
    val_arr.append(mark)
set_val=set(val_arr)
val_arr=list(set_val)
val_arr.sort()
sec_mark=val_arr[1]
final_ar=[]
for i in a:
    if (sec_mark==a[i]):
        final_ar.append(i)
final_ar.sort()
for i in final_ar:
    print(i)
