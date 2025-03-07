'''
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.
'''

def solve(words1, words2):    
    res = []
    hash2 = {}
    for j in words2:
        for k in j:
            hash2[k] = hash2.get(k,0) + 1
        
    for i in words1:
        hash1 = {}
       
        for k in i:
            if k in hash2:
                hash1[k] = hash1.get(k,0) +1
                if hash1[k] > hash2[k]:
                    hash1[k] = hash2[k]
        if hash1 == hash2:
            res.append(i)
       
    return res
from collections import defaultdict
from collections import Counter

def solve2(words1, words2):
    count_2 = defaultdict(int)
    for w in words2:
        count_w = Counter(w)
        for c, cnt in count_w.items():
            count_2[c] = max(count_2[c], cnt)
    res = []

    for w in words1:
        count_w = Counter(w)
        flag = True
        for c, cnt in count_2.items():
            if count_w[c] < cnt:
                flag = False
                break
        if flag:
            res.append(w)

    return res


print(solve2(["amazon","apple","facebook","google","leetcode"], ["lo","eo"])) 

'''
medium problem

idea: O(n * m) but make hashmaps since order of subsets doenst matter (ie "wr" is a subset of "rw")

idk... to many weird things.. had to watch the video

this idea with the sol is to merge the hashmaps by taking the max of each letter freq NOT ADDING. i was super close myself lol
'''