import heapq
heap=[]
heapq.heappush(heap,('v',11))
heapq.heappush(heap,('v1',12))
heapq.heappush(heap,('v3',13))
for a in heap:
    print(a)
heapq.heapify(heap)
print(heap[0])
heapq.heappop(heap)
print(heap)