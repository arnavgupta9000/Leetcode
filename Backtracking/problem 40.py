'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''

def solve(candidates, target):
    res = []
    curr = []
    n = len(candidates)
    candidates.sort()
    def dfs(curr_sum, start):
        if curr_sum == target:
            res.append(curr[:])
            return
        
        if curr_sum > target:
            return
        
        for i in range(start, n):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            curr.append(candidates[i])
            dfs(curr_sum + candidates[i], i+1)
            curr.pop()
    dfs(0,0)
    return res

print(solve([10,1,2,7,6,1,5], 8))

'''
seems to be the same as the first but just have the extra line `if i > start and candidates[i] == candidates[i-1]: skip`

^^ as long as you know that trick it becomes very easy - got it on my own in like <5 mins
'''