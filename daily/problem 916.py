'''
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.
'''

def solve(words1, words2):    
    res = []

    n = len(words1)
    n2 = len(words2)

    for i in words1:
        hash1 = {}
        hash2 = {}
        for j in words2:
            hash2[j] = hash2.get(j,0) + 1
        
        # for k in i:
        #     if k in hash2:
        #         hash1[k] = hash1.get(k,0) +1
        #         if hash1[k] > hash2[k]:
        #             hash1[k] = hash2[k]
        # if hash1 == hash2:
        #     res.append(i)
        var = True
        for key, value in hash2.items():
            x = 0
            while value > 0 and var:
                x = i.find(key, x)
                if x == -1:
                    var = False
                value -= 1
        if var:
            res.append(i)
    return res

print(solve(["amazon","apple","facebook","google","leetcode"], ["lo","eo"])) 


'''
medium problem

idea: O(n * m) but make hashmaps since order of subsets doenst matter (ie "wr" is a subset of "rw")

idk... to many weird things..
'''