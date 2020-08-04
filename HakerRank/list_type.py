ar=[]
n=int(input("Enter num:"))
for i in range(0,n):
    temp_str=input("Enter string:")
    temp_str_arr=temp_str.strip().split(' ')
    cmd=temp_str_arr[0]
    if(cmd=="print"):
        print(ar)
    elif(cmd=="sort"):
        print(ar.sort())
    elif(cmd=="reverse"):
        print(ar.reverse())
    elif(cmd=="pop"):
        print(ar.pop())
    elif(cmd=="count"):
        val=int(temp_str_arr[1])
        print(ar.count(val))
    elif(cmd=="index"):
        val = int( temp_str_arr[1] )
        print(ar.index( val ))
    elif(cmd=="remove"):
        val = int( temp_str_arr[1] )
        print(ar.remove( val ))
    elif(cmd=="append"):
        val = int( temp_str_arr[1] )
        print(ar.append( val ))
    elif(cmd=="insert"):
        pos= int(temp_str_arr[1])
        val = int( temp_str_arr[1] )
        print( ar.insert( pos,val ))
