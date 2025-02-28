'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

def solve(digits):
    dic = {'2': 'abc', '3':"def", '4':"ghi", '5': "jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9': "wxyz"}
    res = []
    def dfs(start, curr):
        if len(curr) == len(digits):
            res.append(curr[:])
            return
        
        for i in range(start,len(digits)):
            for letter in dic[digits[i]]:
                dfs(i+1, curr + letter)


    if digits:

        dfs(0, "")
    return res


    

print(solve("23"))

'''


'''