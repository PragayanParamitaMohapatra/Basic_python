if __name__=="__main__":
    n=int(input("Enter number:"))
    arr=list(map(int,input().rstrip().split()))
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end="")