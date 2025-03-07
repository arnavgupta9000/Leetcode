'''
You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

isPrefixAndSuffix(str1, str2) returns true if str1 is both a 
prefix
 and a 
suffix
 of str2, and false otherwise.
For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

 
'''

def helper(word1, word2):
    if len(word1) > len(word2): #cannot be a prefix or postfix
        return False
    
    return word2[0:len(word1)] == word1 and word2[len(word2) - len(word1):] == word1

def solve(words):
    n = len(words)
    res = 0
    for i in range(n):
        for j in range(i + 1, n): # i + 1 to not include that ith element
            if helper(words[i], words[j]):
                res +=1
    return res



print(solve(["a","aba","ababa","aa"]))

'''
easy problem - not the easiest

intuition: O(n^2 * m) where u loop thorugh the array twice, and then use the helper function to see if its works 
got it in like ~10 mins. the tricky thing is doing word2[len(word2) - len(word1):] 
'''