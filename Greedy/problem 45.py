'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
'''

def solve(nums):
    res = 0

    l, r = 0, 0
    n = len(nums)
    while r < n:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, nums[i])
        res+=1
        l = r+1
        r += farthest
    return res