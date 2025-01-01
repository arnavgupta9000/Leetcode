'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''


def solve(grid):
    def dfs(r,c, curr):
        if ((r,c) in visited or not (0 <= r < len(grid)) or not (0 <= c < len(grid[r])) or grid[r][c] != 1):
            return 1
        visited.add((r,c))
        curr +=1
        curr = max(curr,dfs(r+1, c, curr))
        curr = max(curr,dfs(r-1, c, curr))
        curr = max(curr,dfs(r, c+1, curr))
        curr = max(curr,dfs(r, c-1, curr))
        return curr
    
    # cleanear dfs from chat
    def dfs2(r,c):
        if ((r,c) in visited or not (0 <= r < len(grid)) or not (0 <= c < len(grid[r])) or grid[r][c] != 1):
            return 0
        visited.add((r, c))

        return (1 + dfs2(r + 1, c) + dfs2(r - 1, c) + dfs2(r, c+1) + dfs2(r, c-1))
        

    max_area = 0
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1 and (r,c) not in visited:
                current_area = dfs2(r,c)
                max_area = max(max_area, current_area)
    return max_area

print(solve([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))

'''
this seems similar to problem 200 (prev problem) but now we can just count the number and return it and take the max of it

ok got it on my own but the curr thing in the dfs is def wasted time...
'''