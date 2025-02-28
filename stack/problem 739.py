#Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

def solve(temperatures):
    n = len(temperatures)
    stack = []
    # value, index
    res = [0] * n

    for i in range(n):
        while stack and temperatures[i] > stack[-1][0]:
            value, index = stack.pop()
            res[index] = (i - index)
        stack.append((temperatures[i], i))
    return res



print(solve([73,74,75,71,69,72,76,73]))

'''
no clue on this... ok so my first idea where u just store everything in a stack was right i just thought it would take some extra time since it could become O(n^2) but ig not...
'''