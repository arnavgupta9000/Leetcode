'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
'''

def solve(nums):
    res = []
    curr = []
    count = {}
    n = len(nums)
    for i in nums:
        count[i] = count.get(i,0) + 1
    
    def dfs():
        if len(curr) == n:
            res.append(curr[:])
            return

        for i in count:
            if count[i] > 0:
                curr.append(i)
                count[i] -=1

                dfs()
                count[i] +=1
                curr.pop()
    dfs()
    return res

print(solve([1,1,2]))