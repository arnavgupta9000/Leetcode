'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

'''

def solve(matrix, target):
    l = 0
    r = len(matrix) - 1

    while l <= r:
        mid = (l+r) // 2
        first = matrix[mid][0] # first value in that list
        last = matrix[mid][-1] # last value
        if first <= target <= last:
            # solution might be in here, run another binary search in this list
            l2 = 0
            r2 = len(matrix[mid]) - 1

            while l2 <= r2:
                mid2 = (l2+r2) // 2
                if matrix[mid][mid2] == target:
                    return True
                elif matrix[mid][mid2] < target:
                    l2 = mid2 + 1
                else:
                    r2 = mid2 - 1
            # no solution
            return False

        elif matrix[mid][0] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False

print(solve([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))

'''
first find the mid point of the out list. then check the first element and the last element. if first <= target <= last, then run a linear search on it (or binary again). if not get rid of the half the list

got it on my own!! not to hard, the only problem was using 'l' and 'r' and 'm' in the second binary search instead of 'l2' and 'r2' and 'm2'

idk how to do the conversion to 1d array and then just run binary search on that 1d array...
'''