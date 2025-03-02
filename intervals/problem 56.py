'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

'''

def solve(intervals):
    intervals = sorted(intervals, key = lambda l: l[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = output[-1][1]

        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])
    return output

  


print(solve([[1,3],[8,10],[15,18],[2,6]]))

'''
just watched the vid
'''