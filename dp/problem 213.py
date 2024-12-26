#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

def solve(nums):

    def helper(arr):
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, n):
            dp[i] = max( arr[i] + dp[i-2], dp[i-1] )
        
        return dp[n-1]


    if len(nums) <=2:
        return max(nums)
    if len(nums) == 3:
        return max(max(nums[0], nums[2]), nums[1])
    return max(helper(nums[:-1]), helper(nums[1:]))
    

print(solve([2,1,1,1]))


'''
Intution: just take the max of (arr[:len(n) - 1], arr[1:]), ie splice the list to get rid of the last element, or get rid of the first element

solved without help
'''