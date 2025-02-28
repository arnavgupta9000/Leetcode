'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''
class Check:
    def solve(self,board, word):
        
        if not word or not board:
            return False

        
        def dfs(r,c, pos, visited):
            if pos >= len(word):
                return True
            if (r,c) in visited or (not (0<=r< rows) or not (0<=c < cols) or board[r][c] != word[pos]):
                return

            visited.add((r,c))

            if board[r][c] == word[pos]:
                found = (
                dfs(r+1,c,pos + 1, visited) or
                dfs(r-1,c,pos + 1, visited) or
                dfs(r,c+1,pos + 1, visited) or
                dfs(r,c-1,pos + 1, visited)
                )
            
            visited.remove((r, c))

            return found


            
        
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0, set()):
                        return True

        return False


check = Check()
print(check.solve([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

'''
class Check:
    def solve(self,board, word):
        
        self.res = False
        if not word or not board:
            return False

        
        def dfs(r,c, pos):
            if pos >= len(word):
                self.res = True
                return
            if (r,c) in visited or (not (0<=r< rows) or not (0<=c < cols) or board[r][c] != word[pos]):
                return

            visited.add((r,c))

            if board[r][c] == word[pos]:
                dfs(r+1,c,pos + 1)
                dfs(r-1,c,pos + 1)
                dfs(r,c+1,pos + 1)
                dfs(r,c-1,pos + 1)
            return 


            
        
        rows, cols = len(board), len(board[0])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    dfs(r,c,0)
                if self.res:
                    return True

        return False

og code broke because of 
[["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"
and doesnt back track propely ^^ bc of that
'''