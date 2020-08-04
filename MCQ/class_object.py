class Datacode:
    def __init__(self,x):
        self.x=x
    def count(self,x):
        self.x=self.x+6
class Shootpy(Datacode):
    def __init__(self,y=0):
        Datacode.__init__(self,5)
        self.y=y
    def count(self):
        self.y+=7
def main():
    obj=Shootpy()
    obj.count()
    print(obj.x,obj.y)
main()
