'''
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.


'''

def solve(boxes):
    n = len(boxes)

    left = [0] * n
    right = [0] * n
    res = [0] * n

    balls = 0
    cost = 0 # we need this cost to sum up all the prev costs. ie (1,1,0) => (1,1,3) without cost we would get (1,1,2)
    # forward pass
    for i in range(n):
        left[i] = cost # how much does it cost to move the balls here FROM THE LEFT SIDE ONLY
        if boxes[i] == '1':
            balls +=1
        cost += balls

    cost = 0
    balls = 0

    for i in range(n-1,-1, -1): # backwards pass
        right[i] = cost
        if boxes[i] == '1':
            balls +=1
        cost += balls
    
    for i in range(n):
        res[i] = left[i] + right[i]
    return res


print(solve("110"))


'''
dont know how to use a prefix/postfix sum so gonna try to learn about it through this

so basically u just go through the array twice once forwards and backwards.

on the forward pass u count as u go up the total sum, same with backwards pass

then go through the array one more time and add the left and right passes to get ur ans
'''