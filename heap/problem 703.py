'''
just watched the sol for this one since my heaps understanding wasnt the best atp
'''
import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
'''
Min Heap When to use:

You need to efficiently track the k largest elements or the k-th smallest element.
The smallest element in your current subset should always be accessible at the root of the heap.
Why:

A min heap allows you to efficiently pop the smallest element and maintain the k largest elements in the heap by discarding smaller ones.
Example Problems:

Find the k-th largest element in a stream:
Use a min heap of size k, keeping only the largest k elements. The root (smallest element in the heap) is the k-th largest.
Find the smallest element in a dataset:
Use a min heap directly since the root of the heap is always the smallest.
2. Max Heap
When to use:

You need to efficiently track the k smallest elements or the k-th largest element.
The largest element in your current subset should always be accessible at the root of the heap.
Why:

A max heap allows you to efficiently pop the largest element and maintain the k smallest elements in the heap by discarding larger ones.
Example Problems:

Find the k-th smallest element in a stream:
Use a max heap of size k, keeping only the smallest k elements. The root (largest element in the heap) is the k-th smallest.
Find the largest element in a dataset:
Use a max heap directly since the root of the heap is always the largest.
'''