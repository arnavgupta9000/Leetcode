#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.


def solve(nums):
    nums.sort()
    res = []

    for i in range(len(nums)):
        #Skip duplicate values for nums[i] to avoid generating duplicate triplets.
        #Why? If nums[i] is the same as nums[i-1], any triplets formed with nums[i] will already have been considered.

        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1 # dont want to include element i
        r = len(nums) - 1
        while l < r: # l cannot be r
            k = nums[i] + nums[l] + nums[r]
            if k > 0:
                r -=1
            elif k < 0:
                l+=1 
            else:
                res.append([nums[i], nums[l], nums[r]])
                l+=1
                r-=1
                while l < r and nums[l] == nums[l - 1]: #Skip duplicate values for the left pointer
                    l += 1
                while l < r and nums[r] == nums[r + 1]: #Skip duplicate values for the right pointer
                    r -= 1
                # if we didnt have this it would fail for this test case [2, -1, -1, 1, 1,-1,1,2,2]. so we do need this since leetcode does test for this LOL


    return res

def solve2(nums): # fails...
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        hash = {}

        for j in range(i+1, len(nums)):
            k = 0 - nums[i] - nums[j]
            if k in hash:
                res.append([nums[i], nums[j], hash[k]])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1

            else:
                hash[nums[j]] = nums[j]
    return res


'''
    triplets = []
    for i in range(len(nums)):
        target = -(nums[i])
        d={}
        for j in range(i+1,len(nums)):
            if target - nums[j] in d:
                triplets.append(sorted([nums[i],target-nums[j],nums[j]]))
            else:
                d[nums[j]]=j
                
    return sorted(list(set(map(tuple,triplets))))

'''

print(solve2([-1,0,1,2,-1,-4]))


'''
Brute force = O(n^3) but we could sort the list, go through each element and then use 2 pointers for that element to then find any elements that equal 0. but for this we must sort the arr. notice with a hash map we could do the same. first submission TLE... check leetcode to see prev code but some issues incldue "while l<=r" dont need "=" then we dont need to check if indicies are different as they always will be (ie dont need i != r != l != i) but the biggest problem is "[nums[i], nums[l], nums[r]]"

u can also solve this using the hashmap way inside the first for loop but that comes with O(n) memory (vs the O(1) with 2 pointers) and is generally slower in some cases, hence this way is preferred but u can still use the hash map way, altho hash map way cant solve dups? so dont use it ig
'''