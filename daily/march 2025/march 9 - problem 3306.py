'''
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

'''

from collections import defaultdict
def solve(word, k):
    def atleastk(k):
        vowel = defaultdict(int)
        non_vowel = 0
        res = 0
        l = 0

        for r in range(len(word)):
            if word[r] in "aeiou":
                vowel[word[r]] +=1
            else:
                non_vowel +=1
            while len(vowel) == 5 and non_vowel >=k:
                res += (len(word) - r)

                if word[l] in "aeiou":
                    vowel[word[l]] -=1
                else:
                    non_vowel -=1
                if vowel[word[l]] == 0:
                    vowel.pop(word[l])
                l+=1
        return res
    return atleastk(k) - atleastk(k+1)


print(solve("ieaouqqieaouqq", 1))

'''
medium

couldnt solve... neetcode even said  its a tricky medium

dont get sol...
'''