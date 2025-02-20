'''

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

def solve(nums):
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

print(solve([1,2,3,4]))

'''
sorta knew to use prefix/postfix from other sources and it makes sense bnut had to watch neetcode/use chat to solve it...
'''