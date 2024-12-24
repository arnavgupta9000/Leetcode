#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

def solve(nums):
    
    def dfs():
        if len(curr) == len(nums):
            res.append(curr[:])
            return
        
        for i in range(len(nums)):
            # skip if the element is already used in this permutation (to avoid duplicates)
            if nums[i] in curr:
                continue

            curr.append(nums[i])
            dfs()  
            curr.pop()  


    curr = []
    res = []
    dfs()
    return res

def solve1(nums):
    if len(nums) == 0:
        return [[]]
    
    perms = solve1(nums[1:])

    res = []
    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, nums[0])
            res.append(p_copy)
    return res
# this solution is very hard to come up with so i wouldnt recommened it



print(solve([1,2,3]))


'''
Here you cant use the combinations way with a start parameter since that will skip permutations... if we do it that way with the current if statement we have we get combinations but not permutations. this way we can see that each number in arr[i], can appear at a different index in the result variable which is what we want. using the combination way we would skip potential solutions

solution 2 (solve1() )= neetcode
'''