#Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

#A pair (i, j) is fair if:

#0 <= i < j < n, and
#lower <= nums[i] + nums[j] <= upper

def solve(nums, lower, upper):
    nums.sort()
    count = 0

    for i in range(len(nums) - 1):
        l = i + 1
        r = len(nums) - 1
        
        # Find the smallest index where the sum >= lower
        while l <= r:
            mid = (l + r) // 2
            if nums[i] + nums[mid] >= lower:
                r = mid - 1
            else:
                l = mid + 1
        left_bound = l

        # Reset pointers for the upper bound
        l = i + 1
        r = len(nums) - 1
        
        # Find the largest index where the sum <= upper
        while l <= r:
            mid = (l + r) // 2
            if nums[i] + nums[mid] <= upper:
                l = mid + 1
            else:
                r = mid - 1
        right_bound = r

        # Add the number of valid pairs for this `i`
        count += max(0, right_bound - left_bound + 1)

    return count


    

print(solve([0,1,7,4,4,5], 3, 6))


'''
intuition: o(n^2) just run a double for loop, but lets try sorting the list and doing something with one pass to get O(n)
'''