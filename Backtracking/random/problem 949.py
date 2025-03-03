'''
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.
'''

def solve(arr):
    res = ""

    def is_valid(time):
        hh, mm = int(time[:2]), int(time[2:])
        return 0 <= hh < 24 and 0 <= mm < 60

    def dfs(path, count):
        nonlocal res
        if len(path) == 4:
            time = "".join(path)
            if is_valid(time):
                res = max(res, time)  # Store lexicographically max valid time
            return

        for digit in count:
            if count[digit] > 0:
                count[digit] -= 1
                dfs(path + [str(digit)], count)
                count[digit] += 1  # Backtrack

    count = {}
    for i in arr:
        count[i] = count.get(i,0) + 1
    dfs([], count)

    return res[:2] + ":" + res[2:] if res else ""




def solve2(arr): # using arr instead of hashmap
    res = ""

    def is_valid(time):
        hh, mm = int(time[:2]), int(time[2:])
        return 0 <= hh < 24 and 0 <= mm < 60

    def dfs(path, used):
        nonlocal res
        if len(path) == 4:
            time = "".join(path)
            if is_valid(time):
                res = max(res, time)  # Compare lexicographically
            return

        for i in range(4):
            if not used[i]:  # Prevent reuse
                used[i] = True
                dfs(path + [str(arr[i])], used)
                used[i] = False

    dfs([], [False] * 4)
    
    return res[:2] + ":" + res[2:] if res else ""

print(solve([1,2,3,4]))