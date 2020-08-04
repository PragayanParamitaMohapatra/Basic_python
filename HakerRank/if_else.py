if __name__=="__main__":
    N=int(input("Enter a number:").strip())
    n=N
    w="weird"
    nw="not weird"
    if n%2==1:
        print(w)
    elif n%2==0 and (n>=2 & n<5):
        print(nw)
    elif n%2==0 and (n >= 6 and n<=20):
        print(w)
    elif n%2==0 and (n>2) :
        print(nw)

