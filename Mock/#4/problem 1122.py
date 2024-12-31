'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
'''

def solve(arr1, arr2):
    hash_map = {}
    result = []

    for num in arr1:
        hash_map[num] = hash_map.get(num, 0) + 1

    for num in arr2:
        if num in hash_map:
            result.extend([num] * hash_map[num])
            del hash_map[num]  

    remaining_elements = sorted(hash_map.keys())
    for num in remaining_elements:
        result.extend([num] * hash_map[num])

    return result

    

print(solve([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))

'''
fisrt thing to note, we have an 10^3 limit hence O(n^2) should suffice
'''