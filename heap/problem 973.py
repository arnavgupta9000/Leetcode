'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''

import heapq
import math
def solve(points, k):
    heap = [] # store a tuple, the distance and the x,y coord

    for i in points:
        distance = math.sqrt((i[0]) ** 2 + i[1] ** 2) # the second coord is 0 but well anything minus 0 is just that thing
        # dont need to take the sqrt() at all 
        if len(heap) < k: # append it no matter what
            heapq.heappush(heap, (-distance, i[0], i[1]))
        else:
            heapq.heappush(heap, (-distance, i[0], i[1]))
            while len(heap) > k:
                heapq.heappop(heap)
    return [[x,y] for _, x, y in heap]

print(solve([[1,3],[-2,2]], 1))


'''
first thing its 'k' closest -> direct hint to using a heap. we have 10^4 at max case so it must be O(n) no slower. hence this all points to a heap problem
remember we want a MAX heap not a min heap, cause we want to get rid of the max numbers NOTT the minimum numbers. that tripped me up

^^ after figuring that out i got it on my own!!

small efficiecy from neetcode vid, we dont nee to take the sqrt() saving time

In Python, you don't initialize a heapq with a function like heapq() directly. Instead, you use a plain list to represent the heap and then operate on it with functions provided by the heapq module. If you want to create an empty heap, you simply initialize an empty list.

# Create an empty heap
heap = []

# Add elements to the heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 15)

# Remove and return the smallest element
smallest = heapq.heappop(heap)

'''