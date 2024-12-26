#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order

def solve(nums, target):
    hash = {}

    for i in range(len(nums)):
        k = target - nums[i]
        if k in hash:
            return (hash[k], i)
        hash[nums[i]] = i
    
    return False
    


print(solve([3,2,4], 6))