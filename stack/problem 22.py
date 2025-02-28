'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

def solve(n):
    res = []
    curr = []
    def dfs(open, close):
        if len(curr) == 2*n: # we need exactly n opening and n closing brackets
            res.append("".join(curr))
            return
        if open < n: # add more open brackets
            curr.append("(")
            dfs(open + 1, close)
            curr.pop()

        if close < open: # need to add closing brackets
            curr.append(")")
            dfs(open, close + 1)
            curr.pop()
    
    dfs(0,0)
    return res

print(solve(3))





'''
looked at sol for this one

'''