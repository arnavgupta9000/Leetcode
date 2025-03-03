#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def solve(nums, k):
    hash = {}
    freq = [[] for i in range(len(nums) + 1)]

    for i in nums:
        hash[i] = hash.get(i,0) + 1
    
    for key, value in hash.items():
        freq[value].append(key)

    res = []

    for i in range(len(freq) - 1, -1, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

import heapq

def solve3(nums,k): # using a heap way after the fact. not as good as bucket sort lol

    count = {}
    for i in nums:
        count[i] = count.get(i,0) + 1
    
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for _, num in heap]

print(solve([1,1,1,2,2,3], 2))


'''
solved with O(n^2) time very slow... should speed this up.

second solution is bucket sort which is O(n) using a clever trick where each outter array is the freq and each inner array is the number 
'''