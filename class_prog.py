# class Count:
#    def __init__(self, count=0):
#       self.__count=count
# a=Count(2)
# b=Count(2)
# print(id(a)==id(b), end = '' '')
#
# c= "hello"
# d= "hello"
# print(id(c)==id(d))


# def func1(n):
#    if(n==0):
#       return 0
#    else:
#       return(n+func1(n-1))
# def func2(n, result):
#    if(n==0):
#       return(result)
#    else:
#       return(func2(n-1, n+result))
# print(func1(4))
# print(func2(4,0))



# num=3
# while True:
#    if (num%0o12 == 0):
#       break
# print(num)
# num += 1

q =( 'a', 'b')
print(3 * q)
def f():
   try:
      print(1)
   finally:
      print(2)
f()
x = ~~~~19
print(x)
s = '\t\t\t\n\nTutorialsPoint\n\n\n\t\t\t'
print(s.strip())
print('Recursive Function')
def factorial(n):
   return(n*factorial(n-1))
factorial(4)