'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''
import collections

def solve(grid):
    def check_neighbors(r,c):
        if (not(0 <= r < rows) or not (0 <= c < cols) or grid[r][c] != 1 or (r,c) in visit):
            return
        visit.add((r,c))
        q.append((r,c))

    rows = len(grid)
    cols = len(grid[0])
    q = collections.deque()
    visit = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r,c))
                visit.add((r,c))
    time = 0

    while q: # while the q is not empty
        current_batch = len(q) # for time = 1,2,3 etc
        for i in range(current_batch):
            r,c = q.popleft() 
            grid[r][c] = -2
            check_neighbors(r+1,c)
            check_neighbors(r-1,c)
            check_neighbors(r,c+1)
            check_neighbors(r,c-1)
        time +=1
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                return -1
    return time - 1


print(solve([[2,1,1],[1,1,0],[0,1,1]]))
'''
idea: do a multi source bfs starting form the rotten oranges. after that check to see if any oranges are not rotten and if so return -1 else return the time

got on my own!!

after wathcing the vid the last for loop (to see if theres any fresh oranges) can be combined with the first for loop, ie if u see a fresh orange add 1 to a counter, and then see if at the end the counter == 0 => solution else no solution

the reason we have time - 1 is because lets say we get 

[[2], [1]]. then at time = 0 we append [1] to the que. now time is 1. but then we expend [1] and notice no new things to infect. BUTTT we still increase time. so time = 2. hence we need to subtract 1. alternatively we could only increase time if there was a fresh tomatoe that was rotted in that cycle
'''