'''
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
'''

def solve(a, b):
    n = len(a)
    res = []

    hash = {}  
    cost = 0

    for i in range(n):
        if a[i] in hash:
            cost +=1
        else:
            hash[a[i]] = 1
        if b[i] in hash:
            cost +=1
        else:
            hash[b[i]] = 1
        
        res.append(cost)
    return res


print(solve([1,3,2,4], [3,1,2,4]))


'''
medium problem

seems like we can just keep a dic and add all res

ok solved very fast with no help. not a very hard problem. we have O(n) time
'''