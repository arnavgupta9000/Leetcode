#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def solve(s,t):
    hash1 = {}
    hash2 = {}
    for i in s:
        hash1[i] = hash1.get(i,0) + 1
    for i in t:
        hash2[i] = hash2.get(i,0) + 1
    return hash1 == hash2

print(solve("rat", "car"))