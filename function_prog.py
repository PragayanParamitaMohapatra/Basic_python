# def writer():
#     title="sir"
#     name=(lambda x:title+''+x)
#     return name
# who=writer()
# print(who('author'))

# num1=3*5
# num2=3*5.0
# print(num1==num2)

# print(type(print("9")))

x=2
y=0
def g():
    global x,y
def adder():
    g()
    x=3
    y=1
    x=x+y
print(x)
adder()
print(x)