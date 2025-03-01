'''
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.
'''
from queue import deque
def solve(grid):
    directions = {1:[0,1], 2:[0,-1], 3:[1,0], 4:[-1,0]}

    rows, cols = len(grid), len(grid[0])

    q = deque() # r, c, cost]
    q.append((0,0,0))
    min_cost = {(0,0): 0}

    while q:
        r, c, cost = q.popleft()

        if (r,c) == (rows - 1, cols - 1): #reached target
            return cost
        
        for d in directions:
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc
            n_cost = cost if d == grid[r][c] else cost + 1
            if (nr < 0 or nc < 0 or nr == rows or nc == cols or n_cost >= min_cost.get((nr, nc), float("inf"))):
                continue
            
            min_cost[(nr, nc)] = n_cost
            if d == grid[r][c]:
                q.appendleft((nr,nc,n_cost))
            else:
                q.append((nr,nc, n_cost))
    
print(solve([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))

'''
hard problem so just watched vid

0-1 bfs
'''