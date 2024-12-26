#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def solve(n):
    if n == 0 or n==1:
        return 1
    dp = [0] * (n)
    dp[0] = 1 # 1 stair
    dp[1] = 2 # 2 stairs
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]

print(solve(5))

