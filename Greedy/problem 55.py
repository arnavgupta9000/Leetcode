'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

'''

def solve(nums):
    goal = len(nums) - 1

    for i in range(goal, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal <= 0



print(solve([2,3,1,1,4]))


'''
just watched the vid for this one

so u have start from the other side of th array and make a goal and shift that towards index 0. if they overlap its true otherwise its false
'''