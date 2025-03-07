'''
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.


'''

def solve(grid):
    hash = {}

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1 and i in hash :
                res += hash[i]
            if grid[i][j] == 1 and j in hash :
                res += hash[j]
            if grid[i][j] == 1:
                hash[i] = hash.get(i, 0) + 1
                hash[j] = hash.get(j,0) + 1
    return res



print(solve([[1,0],[1,1]]))

'''
medium problem

watched neetcode... couldnt get
'''