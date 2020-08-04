n=int(input("Enter a number:"))
if n>1:
    for x in range(2,n):
        if(n%x)==0:
            print("not prime number")
            break
        else:
            print("prime")
            break
else:
    print("not prime")