'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
'''

def solve(nums):
    slow, fast = 0, 0

    while True: # fast and slow will always be in bounds
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2:
            return slow

print(solve([1,3,4,2,2]))

'''
basically even neetcode said it memorize this solution, watch the vid u want the intution on why it works

u know 0 is not part of the cycle for sure
'''