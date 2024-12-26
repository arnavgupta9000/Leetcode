#You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

#You can either start from the step with index 0, or the step with index 1.

#Return the minimum cost to reach the top of the floor.

def solve(cost):
    n = len(cost)
    dp = [0] * n

    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] +min(dp[i-1], dp[i-2])
    return min(dp[n-1], dp[n-2]) # if we couldnt start at index 1 we would have to say "return dp[n-1]" (and werent allowed to overshoot), if we are allowed to overshoot regardless of weather or not we start at index 1 we must return "min(dp[n-1], dp[n-2])"

print(solve([1,100,1,1,1,100,1,1,100,1]))

