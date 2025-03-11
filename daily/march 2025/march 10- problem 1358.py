'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.
'''

def solve(s):
    hash = {"a": 0, "b": 0, "c": 0}

    l = 0
    res = 0
    r = 0
    while r < len(s):
        if s[r] in hash:
            hash[s[r]] +=1

        while 0 not in hash.values():
            res += len(s) - r 
            hash[s[l]] -=1
            l+=1
        r+=1
    return res

print(solve("aaacb"))


'''
medium

like yesterdays problem but much much easier lol

solved in like 5 mins
'''