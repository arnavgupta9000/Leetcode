'''
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

have to really view the imgs to get it
'''
from queue import deque
def solve(colors, k):
    res = 0
    for i in range(k):

        colors.append(colors[i])
    broken = deque()
    prev = colors[0] # since 3 <= colors.length
    i = 1
    l=0
    while i < len(colors):
        while i < k:
            if colors[i] == prev:
                broken.append((i-1, colors[i]))
            else:
                prev = colors[i]
            i+=1
        print(colors[l:i])
        if broken and l > broken[0][0]:
            _, color = broken.popleft()

        if not broken:
            res +=1
        
        if prev == colors[i]:
            broken.append((i-1, colors[i]))
        else:
            prev = colors[i]
        i+=1
        l+=1
    
    return res


def solve2(colors, k):
    n = len(colors)
    l = 0
    res = 0

    for r in range(1, (n+k-1)):
        if colors[r % n] == colors[(r-1) % n]:
            # the mod n is since its a circular array right? but instead of extending the array this trick works, if we go out of bounds by 1 its just n+1 % n = 1
            # not alternating shift left to right
            l = r
        if r - l + 1 > k:
            l+=1
        if r - l + 1 == k:
            res +=1
        

    return res


print(solve2([0,1,1], 3))


'''
medium

so first time got 437/625 but WA to [0,1,1] k = 3

then after i fixed the one bug i got it yay! in like ~30 mins with a 10 min dinner break in between p good imo (i was really happy)

solve2 is watching neetcodes video
'''