'''
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
'''


def solve(s):
    hash1 = {"0":0, "1":0}
    hash2 = {"0":0, "1":0}
    score = 0
    for i in s:
        hash1[i] = hash1.get(i, 0) + 1
    for i in range(len(s) - 1):
        if hash1[s[i]] > 0:
            hash1[s[i]] -=1
        hash2[s[i]] = hash2.get(s[i],0) + 1
        res = hash2["0"] + hash1["1"]
        score = max(score, res)
    return score

# a more efficient solution (in terms of memory)

def solve2(s):
    right = s.count('1')
    left = 0
    res = 0 # since "right" right now is not valid
    for i in range(len(s) - 1):
        if s[i] == '0':
            left +=1
        else:
            right -=1
            right = max(right, 0)
        res = max(res, left + right)
    return res
        

print(solve2("011101"))
'''
Jan 1 2025. Easy problem.

seems like we can just use a hashmap and count using 2 pointers
'''