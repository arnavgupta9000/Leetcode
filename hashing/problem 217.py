#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def solve(arr):
    hash = {}

    for i in arr:
        if i in hash:
            return True
        hash[i] = True
    return False

print(solve([1,2,3,1]))