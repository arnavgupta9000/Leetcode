#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

def solve(s):
    if s == "":
        return True
    s = s.lower()
    r = len(s) - 1
    l = 0
    while l <=r:
        if not (s[l].isalpha() or s[l].isnumeric()):
            l+=1
            continue
        if not (s[r].isalpha() or s[r].isnumeric()):
            r-=1
            continue
        if s[r] != s[l]:
            return False
        l+=1
        r-=1
    return True

def solve2(s): # another way to solve it but slightly worse as it uses O(n) memory whereas 2 pointers uses O(1) memory, both are O(n) time complexity
    if s == '':
        return True
    new = ''
    for i in s:
        if i.isalpha() or i.isnumeric():
            new += i.lower()
    if new == new[::-1]:
        return True
    return False

print(solve("A man, a plan, a canal: Panama"))

