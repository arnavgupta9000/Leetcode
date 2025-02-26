'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''

def solve(nums):
    if not nums:
        return -float('inf')
    res = nums[0]
    window = 0
    for i in nums:
        if window < 0:
            window = 0
        window += i
        res = max(res, window)
    return res
    


'''
can just use kanade's algo
'''