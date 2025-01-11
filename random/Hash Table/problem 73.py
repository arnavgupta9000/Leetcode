'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''


def solve(matrix):
    hash = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                hash.add((i,j))
    while hash:
        i,j = hash.pop()

        # go right and left
        for k in range(len(matrix[i])):
            matrix[i][k] = 0
        # go up and down 
        for k in range(len(matrix)): # this line
            matrix[k][j] = 0
    return matrix

print(solve([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))


'''
idea just have a double loop. when u get a 0, go left, right, up and down making everything 0

got it, took ~12 mins, one part of the problem was "#this line" it doesnt need len(matrix[i]), just len(matrix)
'''