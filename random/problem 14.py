'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

def solve(strs):
    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res


def solve2(strs):
    strs.sort()  # Sort lexicographically (O(N log N))
    
    first, last = strs[0], strs[-1]  # First and last words after sorting
    i = 0
    
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    
    return first[:i]  # Common prefix between first and last words


print(solve(["flower","flow","flight"]))