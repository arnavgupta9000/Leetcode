'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

def solve(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    # squares = [set() for _ in range(9)]
    squares = [[set() for _ in range(3)] for _ in range(3)]


    for r in range(9):
        for c in range(9):
            tile = board[r][c]
            if not tile == ".":
                r_index, c_index = r // 3, c // 3
                if ((tile in rows [r])
                    or (tile in cols[c])
                    # or tile in squares[r_index * 3 + c_index]):
                    or tile in squares[r // 3][c // 3]):
                    return False
                rows[r].add(tile)
                cols[c].add(tile)
                squares[r // 3][c // 3].add(tile)
    return True



print(solve([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

'''

'''