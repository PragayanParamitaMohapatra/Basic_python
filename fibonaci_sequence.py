a=0
l=[0,1]
while True:
    fib=l[a-1]+l[a]
    a+=1
    l.append(fib)
    print(l)