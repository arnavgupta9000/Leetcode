'''
1408. String Matching in an Array

Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string
'''

def solve(words):
    words = sorted(words, key=len)
    res = []
    for i in range(1, len(words)):
        for j in range(0, i):
            if words[j] in words[i] and words[j] not in res:
                res.append(words[j])
    return res

print(solve(["leetcoder","leetcode","od","hamlet","am"]))

'''
easy problem

solved in 7 mins using O(n^2)?
'''