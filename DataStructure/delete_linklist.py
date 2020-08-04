class Node():
    def __init__(self,data):
     self.data=data
     self.head=None

class LinkedList:

        # Function to initialize head
        def __init__(self):
            self.head = None

        # This function is in LinkedList class. It inserts
        # a new node at the beginning of Linked List.
        def push(self, new_data):
            # 1 & 2: Allocate the Node &
            #     Put in the data
            new_node = Node( new_data )

            # 3. Make next of new Node as head
            new_node.next = self.head

            # 4. Move the head to point to new Node
            self.head = new_node
        def getCount(self):
            temp=self.head
            c=0
            while(temp):
                c +=1
                temp=temp.next
            return c
        def deleteList(self):
            current=self.head
            while(current):
                prev=current.next
                del current.data
                current=prev

        def search(self, x):

            # Initialize current to head
            current = self.head

            # loop till current not equal to None
            while current != None:
                if current.data == x:
                    return True  # data found

                current = current.next

            return False  # Data Not found
if __name__=='__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print ("Count of nodes is :",llist.getCount())
    llist.deleteList()
    if llist == []:

     print( "Linked list deleted" )
    else:
        print("not deleted")
    print ("Count of nodes is :",llist.getCount())
    if llist.search( 21 ):
        print( "Yes" )
    else:
        print( "No" )


