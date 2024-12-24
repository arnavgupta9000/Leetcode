#Given an integer array nums that may contain duplicates, return all possible subsets(the power set).

#The solution set must not contain duplicate subsets. Return the solution in any order.


def solve(nums):

    def dfs(start):
        res.append(curr[:])  # append the current subset
        
        for i in range(start, n):
            # skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            curr.append(nums[i])  
            dfs(i + 1)  
            curr.pop() 

    nums.sort()
    n = len(nums)
    curr = []
    res = []
    dfs(0)
    return res

print(solve([1,2,2]))