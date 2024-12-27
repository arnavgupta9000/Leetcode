#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

#Find two lines that together with the x-axis form a container, such that the container contains the most water.

#Return the maximum amount of water a container can store.

#Notice that you may not slant the container.


def solve(height):
    res = 0

    l = 0
    r = len(height) - 1
    while l < r:
        total = min(height[l], height[r])
        res = max(res, total * (r-l))
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
        
    return res

print(solve([1,8,6,2,5,4,8,3,7]))

'''
just use 2 pointers cause this will always maximize the water. solved by myself. the reason we have l and r is because that maximizes the width instantly. thus we can move the pointers inwards without missing any solutions. if height[l] == height[r], it doesnt matter which pointer we shift
'''