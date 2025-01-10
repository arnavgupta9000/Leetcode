'''
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.
'''


def solve(words, pref):
    res = 0
    for i in words:
        if pref in i[0:len(pref)]:
            res +=1
    return res

print(solve(["leetcode","win","loops","success"], "code"))


'''
easy problem

solved in like 3 mins
'''