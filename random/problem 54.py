#Given an m x n matrix, return all elements of the matrix in spiral order.

def solve(matrix):
    right = len(matrix[0])
    left = 0
    down = len(matrix)
    up = 0
    res = []
    while up <= down and left <= right:
        # for going right
        pass 


print(solve([[1,2,3],[4,5,6],[7,8,9]]))

'''
idea 
'''