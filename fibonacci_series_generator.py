# def fib(num):
#     a,b=0,1
#     for y in range(0,num):
#         yield"{}:{}".format(y+1,a)
#         a,b=b,a+b
# for item in fib(10):
#     print(item)


def fib(num):
    a,b=0,1
    for i in range(num):
        yield a
        a,b=b,a+b
num=int(input("Enter a number:"))
for i in fib(num):
            print(i)