#Given an m x n matrix, return all elements of the matrix in spiral order.

def solve(matrix):
    if not matrix or not matrix[0]:
        return []

    left = 0
    right = len(matrix[0]) - 1
    up = 0
    down = len(matrix) - 1

    res = []

    while left <= right and up <= down:
        # left to right
        for i in range(left, right + 1):
            res.append(matrix[up][i])
        up += 1

        # up to down
        for i in range(up, down + 1):
            res.append(matrix[i][right])
        right -= 1

        # right to left
        if up <= down:
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1

        # go left to right
        if left <= right:
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res

# neetcode
def solve2(matrix):
    res = []
    left, right = 0, len(matrix[0])
    up, down = 0, len(matrix)

    while left < right and up < down:
        # get every i in the up row
        for i in range(left, right):
            res.append(matrix[up][i])
        up +=1

        # get every i in the right col
        for i in range(up, down):
            res.append(matrix[i][right - 1]) # right out of bounds
        right -=1

        if not (left < right and up < down):
            break
        
        # get every i in the bottom row

        for i in range(right - 1, left - 1, -1):
            res.append(matrix[down - 1][i])
        
        down -=1
        for i in range(down - 1, up - 1, -1):
            res.append(matrix[i][left])
        
        left +=1
    return res
        

print(solve2([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

'''
idea

solved with chats help, was pretty close on my own
'''