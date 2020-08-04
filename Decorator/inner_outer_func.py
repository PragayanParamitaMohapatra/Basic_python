def outer():
    print("outer function is started")
    def inner():
        print("ineer function execution")
    print("outer function return inner func")
    return  inner
f1=outer()
f1()
