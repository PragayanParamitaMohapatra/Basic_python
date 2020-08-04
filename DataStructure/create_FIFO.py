# Queue
import queue
q=queue.Queue()
# add element at the end of the queue
for x in range(6):
    q.put(x)
#   remove eleemnt from head of the queue
while not q.empty():
   print(q.get(),end=" ")

