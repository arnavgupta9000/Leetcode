'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
'''

import heapq

def solve(nums, k):
    # we want a max heap not a min heap
    nums = [-i for i in nums]
    heapq.heapify(nums) # O(n)
    while k > 0:
        res = heapq.heappop(nums)
        k-=1
    return -res

print(solve([3,2,1,5,6,4], 2))



'''
again k-th largest points to heap. we have 1 <= k <= 10^5 so we def want a linear time not a nlogn even tho that might work. this all points to using a heap.
notice this problem looks really similar to the previous one (973)

ok i got this one in like 2 mins on my own! very easy for some reason lmao. notice the time is O(n + klogn) = O(klogn) due to us doing heap operations for each iteration and those heap operations take logn time. this is faster if k << n but where k~n its not faster than sorting

ok this one is tricky there is a better algo (altho the heap way works) thats faster called quick SELECT (not quicksort?)
'''