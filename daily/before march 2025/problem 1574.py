#Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

#Return the length of the shortest subarray to remove.

#A subarray is a contiguous subsequence of the array.

def solve(arr):
    #prefix
    n = len(arr)
    r = n-1
    while r > 0 and arr[r - 1] <= arr[r]:
        r-=1
    
    res = r
    
    # remove the postifx
    l = 0
    while l + 1 < n and arr[l] <= arr[l+1]:
        l+=1

    res = min(res, n - 1 - l)

    # remove middle
    l,r = 0, n -1
    while l < r: # why not <=? u want all the elements BETWEEN them 
        # shrink the window
        while l + 1 < r and arr[r - 1] <= arr[r] and arr[l] <= arr[r]:
            r -=1

        # expand invalid window
        while r < n and arr[l] > arr[r]:
            r+=1

        
        res = min(res, r- l - 1)
        if arr[l] > arr[l+1]:
            break
        l+=1
    return res






'''
'''