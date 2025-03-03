def solve(arr) :
    l = 0
    r = len(arr) - 1
    min_value = arr[0]
    while l <= r:
        mid = (l+r) // 2
        min_value = min(min_value, arr[mid])

        if arr[mid] >= arr[0]:
            l = mid + 1
        else:
            r = mid - 1
    return min_value
