#You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

#Return the length of the longest substring containing the same letter you can get after performing the above operations.

def solve(s, k):
    count = {}
    res = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        while (r-l+1) - max(count.values()) > k: # replacements, if its less than k the window is valid, so greater than k means invalid
            count[s[l]] -= 1
            l+=1

        res = max(res, r-l+1)
    return res

def solve2(s,k):

    count = {}
    res = 0

    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxf = max(maxf, count[s[r]])

        while (r-l+1) - maxf > k: # replacements
            count[s[l]] -= 1
            l+=1

        res = max(res, r-l+1)
    return res

print(solve("AABABBA", 1))

'''
no clue how to solve initally had to watch vid...

so basically when using sliding window, u have 2 pointer l, r and u expand r until some condition in the algo. then u start counting up l while the condition is still false. as soon as the conidtion is true, u go back to incrementing r

there is a true O(n) sol (we use O(26n) in sol 1) but it is very hard to find so i wouldnt worry about it to much but

basically for sol2 we say that once we have a max freq, we never lower it since were already over estimating the true cost.

(r - l + 1) - max(count.values())

This calculates how many characters in the window are NOT the most frequent character.
These are the characters we would need to replace to make the entire window the same character.
Checking against k

If the number of characters to replace ((r - l + 1) - max(count.values())) is greater than k, the window is invalid.
In that case, we need to shrink the window from the left (l += 1) to make it valid again.

'''