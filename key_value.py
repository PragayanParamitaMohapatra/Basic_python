n=int(input("Enter number:"
            ))
phonebook={}
for i in range(n):
    l1=list(map(str,input().split()))
    key=l1[0]
    value=l1[1]
    phonebook[key]=value
while True:
    try:
        name=input("Enter name:")
        if name in phonebook:
            print(name+":"+phonebook[name])
        else:
            print("not found")
    except:
        break