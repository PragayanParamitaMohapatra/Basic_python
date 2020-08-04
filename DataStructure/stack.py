class StackDs():
    def  __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()

    #if is empty or not
    def is_empty(self):
        return self.items==[]
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
s=StackDs()

s.push("A")
s.push("B")
print(s.get_stack())