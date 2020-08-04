class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_after_node(self,prev_node,data):
        if not  prev_node:
            print("previous node is not there")
            return
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node



list1=LinkedList()
list1.append("A")
list1.append("B")
list1.append("C")
list1.append("D")
list1.prepend("E")
print(list1.head.next.data)
list1.insert_after_node(list1.head.next,"f")

list1.print_list()