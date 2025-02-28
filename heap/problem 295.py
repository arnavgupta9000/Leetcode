'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''
import heapq
class MedianFinder:

    def __init__(self):
        # two heaps, large, small with minheap, maxheap respectively
        # want the lists to be equal (or differ by at most 1)
        self.small = []
        self.large = []       

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num) # always add value to max heap

        # make sure every num in small <= every num in large

        if (self.small and self.large and -self.small[0] > self.large[0]): #lists are non null and the order is not maintained
            # pop from small, and add to large
            val = -heapq.heappop(self.small) # pop from the max heap and add to min heap
            heapq.heappush(self.large, val)

         # uneven size? order of these 2 if statements dont matter!
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small) # pop from the max heap and add to min heap
            heapq.heappush(self.large, val)
        # always reorder the heaps in this order. because if we have like [-4,-1] and [2,3] we get [-1], [2,3,4] then we resize again to get [-2,-1], [3,4]

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large) # pop from the max heap and add to min heap
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2

x = MedianFinder()
x.addNum(1)
print(x.findMedian())
x.addNum(2)
print(x.findMedian())
x.addNum(3)
print(x.findMedian())
x.addNum(4)


'''
hard problem... sorta saw that we needed 2 inital heaps - 1 min and max so we'll go from there

couldnt solve on my own.. its a hard problem after all...

wow super clever, have the MAX heap be for the SMALLER numbers and the MIN heap be for the BIGGER numbers

ex [1,2] [3,4]

the max heap is for 1,2 and the min heap is for 3,4 since taking the max of [1,2] is O(1) and taking the min of(3,4) is O(1)

when we have an odd length like 5 elements total if 3 ele in max heap look at top of max heap else look at top of min heap. notice its always O(1)

always want to make sure that max heap values <= min heap values

there is a lot of things to constantly check...
'''