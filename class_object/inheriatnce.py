class A:
    def __init__(self,x=0):
        self.x=x
    def func1(self):
        self.x+=1
class B(A):
    def __init__(self,y=0):
        A.__init__(self,3)
        self.y=y
    def func1(self):
        self.y+=1
def main():
    b=B()
    b.func1()
    print(b.x,b.y)
main()