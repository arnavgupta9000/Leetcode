'''
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.
'''
import heapq
from queue import deque
def solve(tasks, n):
    count = {}
    for i in tasks:
        count[i] = count.get(i,0) + 1
    heap = [-i for i in count.values()]

    heapq.heapify(heap)

    time = 0
    q = deque() # pair of items if [-count, time]
    while heap or q:

        if heap:
            count = heapq.heappop(heap) + 1
            if count != 0:
                q.append([count, time + n])
        if q and q[0][1] == time: # if idle time of first item of q
            heapq.heappush(heap, q.popleft()[0])
        time +=1

    return time

print(solve(["A","A","A","B","B","B"], 2))



'''
watched the vid

the intuition is you do the most freq task first than the less freq tasks later
'''