'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

def solve(s):
    stack = []

    for i in s:
        if i in ')]}':
            if not stack:
                return False
            element = stack.pop()
            if (i == ')' and element != '(') or (i == ']' and element != '[') or (i == '}' and element != '{'):
                return False
        
        else:
            stack.append(i)
    return stack == []

print(solve())