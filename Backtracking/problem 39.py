#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

#The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequencyof at least one of the chosen numbers is different.

#The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input

def solve(candidates, target):

    def dfs(curr_sum, start):
        if curr_sum == target:
            res.append(curr[:])
            return
        
        if curr_sum > target:
            return
        
        for i in range(start, len(candidates)):
            curr.append(candidates[i])
            dfs(curr_sum + candidates[i], i)
            curr.pop()
        return
    
    res = []
    curr = []
    dfs(0,0)
    return res

print(solve([2,3,6,7], 7))

'''
Intuition: got a WA because of bad handling with duplicates. basically we dfs and if the current sum == target we add it, if the currrent sum > target, we need to backtrack

if we did i+1 in the recursive call, it would make it so that duplicate of the same elements are not allowed

This also blocked like [2,3,3] and [3,2,2] from appearing since the if 3 was added first it wont ever go back to 2. ie the for loop will start at 1 and never go back to 0 so the 2 in pos 0 can never be reached. if in the dfs call we changed i to be 0, then we would have duplicate solutions where only the order would change. 

we could also do 
if i > start and candidates[i] == candidates[i - 1]:
                continue
                
inside the for loop if we sort candidates first.

The condition i > start checks if the current index i is not the very first index at this level of the recursive call. This is important for the duplicate-skip logic because:

When i == start, it means we are considering the first choice in the current level, so we don't skip any values.
When i > start, it means we've already processed the first choice at this level, so if candidates[i] == candidates[i - 1], we skip candidates[i] to avoid adding duplicate combinations.

'''