'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
'''
import math
def solve(tokens):
    valid = ['+', '-', '*', '/']
    stack = []

    for i in range(len(tokens)):
        if tokens[i] in valid: # pop and append the result
        # if tokens[i] in "+-/*" also works
            num1 = stack.pop()
            num2 = stack.pop()
            if tokens[i] == '/':
                # special case
                # if (num1 < 0 and num2 < 0) or (num1 > 0 and num2 > 0):
                #     stack.append(math.floor(num2 / num1))
                # else:
                #     num1 = abs(num1)
                #     num2 = abs(num2)
                #     num3 = (math.floor(num2 / num1))
                #     stack.append(-num3)
                stack.append(int(num2/num1))

            elif tokens[i] == '+':
                stack.append(num1 + num2)
            elif tokens[i] == '-':
                stack.append(num2 - num1)
            else:
                stack.append(num1 * num2)
        else:
            stack.append(int(tokens[i]))

    return stack[-1]

print(solve(["4","13","5","/","+"]))



'''
so this seems like its just a stack. if u get a an operation u pop the top 2 elements, do the operation and put back into stack. truncate towards 0 implies that if we have a negative number we take the positive of it floor it, then put it back into negative form. no need to worry about divide by 0 as given in the question

also dont have to worry about edge cases where the tokens is not valid as again given in the question

got on my own!!

however an improvment can be just for divison its just stack.append(int(num2/num1))

since the int part just chucks the decimal its like int(-1.5) = -1.0 = -1
'''