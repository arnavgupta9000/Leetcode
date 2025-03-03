'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

'''
Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''


# binary search 

# no empty list

#[1] -> [1]

'''
l =0, r= len(nums) - 1, mid (l+r) // 2, 7//2 -> 3 (7)
target = 7 -> true
target = 4
target = 3, would not be arr

target = 1
(0+9) // 2 = 4 -> element 9
[4,5,6, 7, 9, 12 ,0,1,2]-> merge sort
'''