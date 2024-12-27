#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

#Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

#The tests are generated such that there is exactly one solution. You may not use the same element twice.

#Your solution must use only constant extra space.

def solve(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l<=r:
        k =  numbers[l] + numbers[r]
        if k == target:
            return (l+1, r+1)
        if k > target:
            r-=1
        else:
            l+=1
    return False

print(solve([2,7,11,15],9))



'''
first thing to notice is that we can only use constant extra space ie mem = O(1), aka no hash map => 2 pointers. its 2 pointers since O(1) mem AND the input array is already sorted basically hinting to use 2 pointers

binary search is  O(logn) but not possible, so this is the fastest solution

'''