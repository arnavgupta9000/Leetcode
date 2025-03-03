'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

# at least one element
# 2d array, nested array.length == 2, each element is a pair

'''
Input: intervals = [[1,3],[2,6], [8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

[[1,3],[2,6], [8,10],  [4,12],  [15,18]]
[[1,12], [15,18]]

O(nlogn) -> sort O(nlogn + n) = O(nlogn)
O(n) -> O(1)
[[1,2], [4,5], [9,10]]
[[starti, endi],]
'''

# [1,4], [4,6]
# [1,6]

def solve(intervals):
   
    if not intervals: # if len(arr) == 0 -> empty arr
        return []
    intervals = sorted(intervals, key = lambda i:i[0])
    res = [intervals[0]] # a list of lists

    '''
    intervals =  [[1,4], [2,6]]
    [[1,4], [2,6], [[1,4], [2,6]]


    
    '''

    for start, end in intervals[1:]:
        max_end = res[-1][1] # max_end = 3
        if start <= max_end:
            max_end = max(max_end, end) # [1,4], [2,8]
            res[-1][1] = max_end # 4 -> 8
        else: # [1,4], [6,10]
            res.append([start, end])
    
    return res

# [[1,3],[2,6],[8,10],[15,18]]
# res [[1,6], [8, 10], [15,18]]
# max_end = 6
# is 2 <= 3?
# end = 6. max_end max(3,6) = 6.
# is 8 <= 10 

# max_end = 10
# is 15 <= 10. 
# [[1,6], [8, 10], [15,18]]


# time = O(n)
# space = O(1)