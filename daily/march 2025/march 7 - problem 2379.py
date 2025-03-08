'''
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 
'''

def solve(blocks, k):
    l = 0
    res = float("inf")
    black_box = 0
    for r in range(0, len(blocks)):
        if blocks[r] == "B":
            black_box +=1
        if r >= k:
            if blocks[l] == "B":
                black_box -=1
            l+=1
            res = min(res, abs(black_box - k))
           
    return res

def solve2(blocks, k):
    l = 0
    res = k
    white_box = 0
    for r in range(0, len(blocks)): 
        if blocks[r] == "W":
            white_box +=1

        if r - l + 1 == k: # can change this to r + 1 >=k but its not as efficent according to lc? i mean still tim eso
            res = min(res, white_box)

            if blocks[l] == "W":
                white_box -=1
            l+=1



    return res


print(solve("WBBWWBBWBW", 7))


'''
easy 

watched the vid - saw sliding window in the comments and then tried it

ok i kept getting WA but then i got it. not an easy imo idk
'''