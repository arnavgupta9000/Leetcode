'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
import collections
def solve(grid):

    def bfs(r,c):
        q = collections.deque()
        visit.add((r,c))
        q.append((r,c))
        while q:
            row, col = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                r,c = row + dr, col + dc
                if (0 <=(r) < rows and 0 <=(c) < cols and grid[r][c] == '1' and (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))

    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visit:
                bfs(r,c)
                islands +=1
    return islands

def solve2(grid):
    def dfs(r,c):
        if ((r,c) in visited or not (0 <= r < len(grid)) or not (0 <= c < len(grid[r])) or grid[r][c] != '1'):
            return
        visited.add((r,c))
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    visited = set()
    islands = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (grid[r][c] == '1' and (r,c) not in visited):
                islands +=1
                dfs(r,c)
    return islands
                
print(solve2([
  ["1","1","0","0","0"],
  ["1","0","0","1","0"],
  ["0","0","0","0","0"],
  ["0","0","0","1","0"]
]))

'''
as this is my first graph problem im just gonna watch the video on how to do this

tried the dfs way as well
'''