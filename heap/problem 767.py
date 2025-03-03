'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

'''

import heapq
def solve(s):
    count = {}
    for i in s:
        count[i] = count.get(i,0) + 1
    
    heap = [(-i, key) for key, i in count.items()]
    heapq.heapify(heap)

    prev = None
    res = ""

    while heap or prev:
        if prev and not heap:
            return ""

        #most frequent except prev
        count, char = heapq.heappop(heap)
        res += char
        count += 1 

        if prev:
            heapq.heappush(heap,prev)
            prev = None
        if count != 0:
            prev = (count, char)
    return res

'''

'''