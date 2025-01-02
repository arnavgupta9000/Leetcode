'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
'''

import heapq

def solve(stones):
    stones = [-i for i in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)
        if not (x==y):
            x = abs(x) - abs(y)
            heapq.heappush(stones, -x)
            # heapq.heapify(stones) # dont need this its already maintanied as a heap
    return -stones[0] if stones else 0

print(solve([2,7,4,1,8,1]))

'''
we have to use -i since python only supports min heaps. this way we can use max heaps but just remember to turn the value into the positive version when u take it out

ok solved on my own yay

Question 1: After Using heapify, Is the Heap Property Always Maintained?
Yes, once you use heapify to create a heap, the heap property is automatically maintained for all subsequent operations as long as you only use heapq functions like heappush and heappop.

You never have to manually call heapify again after using these functions because they ensure that the heap remains valid after each operation.

Manual heapify is unnecessary unless:

You directly modify the heap structure (e.g., appending or removing elements without using heapq).
You have a new, unsorted list and want to convert it into a heap.

'''