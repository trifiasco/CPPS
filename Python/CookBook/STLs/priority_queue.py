
from heapq import heappop, heappush

'''
Info - Heaps are binary trees for which every parent node has a value less than or equal to any of its children
- heap[0] is the smallest item, and heap.sort() maintains the heap invariant! (**MIN_HEAP by default**)
- heapq.heappush(heap, item)
- heapq.heappop(heap)
- heapq.heappushpop(heap, item) - push item in heap, and then return the smallest item from the heap.
- heapq.heapify(x) - transform a list(x) into heap
'''

if __name__ == "__main__":

    # basic example
    h = []
    for value in [1, 2, 3, 4, 5, 6]:
        heappush(h, value)

    heapsorted = [heappop(h) for i in range(len(h))]
    print(heapsorted)
    pass
