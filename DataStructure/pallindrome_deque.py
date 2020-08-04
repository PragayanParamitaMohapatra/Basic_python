class Dequeue():
    def __init__(self):
        self.item=[]
    def add_front(self,data):
        self.item.insert(0,data)
    def add_rear(self,data):
        self.item.append(data)
    def remove_front(self):
      return self.item.pop(0)
    def remove_rear(self):
       return self.item.pop()
    def isEmpty(self):
      if (self.item)==[]:
          return True
      else:
          return False

    def size(self):
            return len(self.item)

    def peek_front(self):
       return self.item[0]
    def peek_rear(self):
        return self.item[-1]

def main(data):
    d=Dequeue()
    for char in data:
        d.add_rear(char)
    while d.size()>=2:
        front_item=d.remove_front()
        rear_item=d.remove_rear()
        if rear_item !=front_item:
            return False
        return True
if __name__=="__main__":
    print(main("nitin"))
    print(main("car"))
