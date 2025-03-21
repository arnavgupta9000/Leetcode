'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

def solve(height):
    if not height:
        return 0
    n = len(height)
    l, r = 0, n - 1
    left_max, right_max = height[l], height[r]
    res = 0
    # if there equal its line a single line up it can store 0 water
    while l < r:
        if left_max < right_max:
            l +=1
            left_max = max(left_max, height[l])
            res += left_max - height[l] # never gonna be negative since we update left_max first
        else:
            r -=1
            right_max = max(right_max, height[r])
            res += right_max - height[r]
    return res

print(solve([0,1,0,2,1,0,1,3,2,1,2,1]))



'''
hard problem had to watch neetcode...

'''