'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
'''

def solve(s):
    first_zero = True

    res = ''
    i = 0
    while True:
        var = True
        try:
            if s[i] == " ":
                s = s[i+1:]
                var = False
        except:
            return 0
        if var:
            break
    if s[0] == '-':
        res += '-'
        s = s[1:]
    if s[0] == "+":
        s = s[1:]

    for i in s:
        try:
            if not isinstance(int(i), int):
                continue
        except:
            break

        if i == 0 and first_zero:
            continue
        
        else:
            res += i
            first_zero = False
    if res == "" or res == "-":
        return 0
    res = int(res)
    if res > (2**31) - 1:
        res = (2**31) - 1
    elif res < (-2 **31):
        res = (-2**31)
    return res
print(solve("+1"))


'''
idea: just read through the string as it is
'''