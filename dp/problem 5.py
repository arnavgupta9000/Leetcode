#Given a string s, return the longest palindromic substring in s.

def solve(s):

    def expand(l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        
        return s[l+1:r] # we need l+1 since the string now points to invalid chars. so we need the strings 1 pos over (ie l+1, r-1), but with slicing the [first:second], first includes the first char so we exclude it, and second doesnt include the last char so no work has to be done
    
    max_len = ''
    for i in range(len(s)):
        # for odd lengths
        string = expand(i,i)
        if len(string) > len(max_len):
            max_len = string

        # for even cases choose the next element with it
        string = expand(i,i+1) # i+1 if its out of bounds is handled by the expand function
        if len(string) > len(max_len):
            max_len = string
    
    return max_len

print(solve('babad'))


'''
Had no clue... started with vid but its so old...

Manacher's Algorithm is O(n) but is very hard to implement

instead we do expand around the center for a O(n^2) solution
'''