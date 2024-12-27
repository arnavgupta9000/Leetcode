#Given a string s, find the length of the longest substring without repeating characters.


def solve(s):
    hash = {}
    bounds = 0
    max_l = 0

    l = 0
    r = 0
    while r <= len(s) - 1:
        if s[r] not in hash:
            hash[s[r]] = 1
            bounds +=1
        elif hash[s[r]] == 0:
            hash[s[r]] = 1
            bounds +=1
        
        else:
            # shift the left pointer over
            bounds-=1
            hash[s[l]] = 0
            l+=1
            r-=1
        max_l = max(max_l, bounds)
        r+=1

    return max_l

def solve2(s):
    char = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in char:
            char.remove(s[l])
            l+=1
        char.add(s[r])
        res = max(res, r-l+1)
    return res

print(solve2("abcabcbb"))

'''
use a hash map to see whats in the string and whats not in it. then use a sliding window to set the bounds. once we have set the bounds no need to change it to anything lower. if all chars are unique increase the bounds

solved on my own. however there are some tricks to learn. 1 -> use a 'set()' for doing flags where u dont need the value. 2 -> instead of doing 'r-=1, r+=1' just use a while loop
'''