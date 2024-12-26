#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

def solve(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    
    dp = [0] * (n)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1]) # need this see bottom

    for i in range(2, n):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    return dp[n-1]

print(solve([2,1,1,2]))


'''


Example Where It Fails: nums = [10, 5]
Correct Approach (dp[1] = max(nums[0], nums[1])):
dp[0] = nums[0] = 10
dp[1] = max(nums[0], nums[1]) = max(10, 5) = 10
Final decision:

Maximum profit after the second house: 10.
Incorrect Approach (dp[1] = nums[1]):
dp[0] = nums[0] = 10
dp[1] = nums[1] = 5
Now, the result would incorrectly suggest that robbing the second house is better, even though robbing the first house gives a higher profit.


Intuition
Think of dp[i] as the best possible profit you can make up to house i:

For dp[0], you can only rob house 0.
For dp[1], you must decide: rob house 1 or stick with house 0.
By initializing dp[1] as max(nums[0], nums[1]), you're setting up the optimal "starting point" for future decisions. Without it, your decisions would be based on incorrect assumptions.






'''
