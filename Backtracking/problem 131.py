'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
'''

def solve(s):
    res = []
    curr = []
    n = len(s)
    def palindrome(curr):
        return curr == curr[::-1]
    
    def dfs(start):
        if start == n:
            res.append(curr[:])

        for i in range(start, n):
            if palindrome(s[start: i + 1]):
                curr.append(s[start:i+1])
                dfs(i+1)
                curr.pop()

    dfs(0)
    return res

print(solve("aabb"))

'''
no idea... had to watch the vid
'''