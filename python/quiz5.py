def my_func(a,k):
    print(a)
    print("value of k=",k)
    for x in a:
        if x == k:
            return 'YES'
        else:
            return "NO"
my_func([5894,6968,5858,8772],8772)