# STACK
import queue
q=queue.LifoQueue()
# add element at the head of the queue
for x in range(6):
    q.put(x)
#   remove eleemnt from head of the queue
while not q.empty():
   print(q.get(),end=" ")

