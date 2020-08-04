class Dequeue():
    def __init__(self):
        self.item=[]
    def add_front(self,data):
        self.item.insert(0,data)
    def add_rear(self,data):
        self.item.append(data)
    def remove_front(self):
        if self.item !=[]:
            return self.item.pop()
        return "remove item as no items there"
    def remove_rear(self):
       return self.item.pop(0)
    def isEmpty(self):
      if self.item==[]:
          return True
      else:
          return False

    def size(self):
        if self.item==[]:
            return None
        else:
            return len(self.item)
    def __repr__(self):
      return "object :{}".format(self.item)
    def peek_front(self):
       return self.item[-1]
    def peek_rear(self):
        return self.item[0]
if __name__=="__main__":
    d=Dequeue()
    d.add_front(2)
    d.add_front(5)
    d.add_front("gufdi")
    print("size",d.size())
    print(d.remove_front())
    print(d.remove_rear())
    print("size",d.size())
    print(d.__repr__())

