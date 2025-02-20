#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def solve(s,t):
    hash1 = {}
    hash2 = {}
    for i in s:
        hash1[i] = hash1.get(i,0) + 1
    for i in t:
        hash2[i] = hash2.get(i,0) + 1
    return hash1 == hash2

    # a way to speed this up using only 1 for loop

    n = len(s)
    m = len(t)
    if n != m:
        return False
    hash1 = {}
    hash2 = {}
    for i in range(n):
        hash1[s[i]] = hash1.get(s[i], 0) + 1
        hash2[t[i]] = hash2.get(t[i], 0) + 1
    return hash1 == hash2
        

print(solve("rat", "car"))