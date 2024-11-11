#Given an integer array nums of unique elements, return all possible subsets(the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.

def solve(nums):
    res = []
    curr = []

    def dfs(i):
        if i >= len(nums):
            res.append(curr[:])
            return

        # decision to include nums[i]
        curr.append(nums[i])
        dfs(i + 1)

        # decision to not include nums[i]

        curr.pop() # drop the element we just added
        dfs(i+1)
    
    dfs(0)
    return res

def solve1(nums):
    res = []
    curr = []

    def dfs(start, n):
        res.append(curr[:])

        for i in range(start, n):
            curr.append(nums[i])
            dfs(i+1, n)
            curr.pop()


    dfs(0, len(nums))
    return res



print(solve1([1,2,3]))

'''
the first way is not the way i would have solved it but its the case where we either include or not include nums[i].

the second way is the way i prefer which i have learned based of memory...
'''