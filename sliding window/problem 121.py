#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def solve(prices):
    # just buy when its lowest and update the max for each point
    res = 0
    lowest = float('inf')
    
    for i in range(len(prices)):
        if prices[i] < lowest:
            lowest = prices[i]
 
        res = max(res, prices[i] - lowest)
    return res


print(solve([7,1,5,3,6,4]))
