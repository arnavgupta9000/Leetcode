'''
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

'''

def solve(word, k): # edited the code so no more default dict
    def atleastk(k):
        vowel = {}
        non_vowel = 0
        res = 0
        l = 0

        for r in range(len(word)):
            if word[r] in "aeiou":
                vowel[word[r]] = vowel.get(word[r], 0) + 1
            else:
                non_vowel +=1

            while len(vowel) == 5 and non_vowel >= k:
                res += (len(word) - r) # count valid substrings
                
                if word[l] in "aeiou":
                    vowel[word[l]] -=1
                    if vowel[word[l]] == 0:
                        del vowel[word[l]]  
                else:
                    non_vowel -=1
                
                l+=1
        return res
    return atleastk(k) - atleastk(k+1)
    # by gettin all words with at least k constants - all words with at least (k+1) constants you get k constants only. its a weird trick but good to know none the less


print(solve("ieaouqqieaouqq", 1))

'''
medium

couldnt solve... neetcode even said  its a tricky medium

dont get sol...
'''