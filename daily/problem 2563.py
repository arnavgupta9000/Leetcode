#Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

#A pair (i, j) is fair if:

#0 <= i < j < n, and
#lower <= nums[i] + nums[j] <= upper

def solve(nums, lower, upper):
    nums.sort()
    count = 0

    for i in range(len(nums) - 1):
        left = i + 1
        right = len(nums) - 1

        # Move left pointer to the first element that forms a sum >= lower
        while left <= right and nums[i] + nums[left] < lower:
            left += 1

        # Move right pointer to the last element that forms a sum <= upper
        while left <= right and nums[i] + nums[right] > upper:
            right -= 1

        # If left <= right, all pairs from left to right with nums[i] are valid
        if left <= right:
            count += right - left + 1

    return count

    

    

print(solve([0,1,7,4,4,5], 3, 6))


'''
intuition: o(n^2) just run a double for loop, but lets try sorting the list and doing something with one pass to get O(n)
'''