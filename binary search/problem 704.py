#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

def solve(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r=mid - 1
        else:
            l = mid + 1
    return -1


'''
just straight binary search

notice that for overflow error (ie l, r are very close to 2^31 (wont happen in python but) then adding might result in overflow. in this case do mid = (l + (r-l)) // 2  )
'''