import queue
# creating queue
p=queue.Queue()
q=queue.Queue()
for x in range(8):
    p.put(x)
print(p.empty())
print(q.empty())
