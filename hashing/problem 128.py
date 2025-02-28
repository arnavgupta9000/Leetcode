'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''


def solve(nums):
    num_set = set(nums)

    res = 0
    for i in num_set:
        if i - 1 not in num_set:
            length = 1
            while i + length in num_set:
                length+=1
            res = max(res, length)
    return res

print(solve([100,4,200,1,3,2]))

'''
had to watch the vid

why is this O(n)? its because each element in the while loop is only processed once. since we check if `i-1` not in res. ie the numbers 4,3,2 would all not go into the if statement thus skipping it. then when we do the while loop they are processed. but notice the `i-1` is O(1) time not O(n) thus its O(1 * n) = O(n)
'''