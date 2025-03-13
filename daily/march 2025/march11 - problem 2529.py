'''
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Follow up: Can you solve the problem in O(log(n)) time complexity?
'''

def solve(nums): # O(n)
    pos = 0
    neg = 0
    for i in nums:
        if i < 0:
            neg +=1
        elif i > 0:
            pos +=1
    return max (neg, pos)

def solve2(nums): # O(logn)

    l = 0
    r = len(nums)
    neg = 0
    pos = 0
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] < 0:
            # everything to the left of mid is negative
            neg += mid - l
            l=mid+1
        elif nums[mid] > 0:
            pos += r - mid
            r=mid-1
        else:
            # linear scan to the left
            mid2 = mid
            while nums[mid] == 0 and mid > l:
                mid -=1
            if mid > l:
                if nums[mid] < 0:
                    neg += mid - l + 1
                    l = mid2 + 1
                else:
                    pos += r - mid
                    r = mid2 - 1 + 1
            else:
                l = mid2 + 1

    return max(neg,pos)

print(solve2([-3,-2,-1,0,0,1,2]))


'''
easy - solved in like 2 seconds

follow up is a bit harder - gave up i hate binary search
'''