#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

#In other words, return true if one of s1's permutations is the substring of s2.


def solve(s1, s2):
    size = len(s1)

    hash1 = {}
    hash2 = {}

    for i in s1:
        hash1[i] = hash1.get(i,0) + 1
    
    if len(s2) < len(s1): # if s1 < s2 it cannot be a permutation
        return False
    
    l = 0
    j=0
    r=0
    while l < len(s2) and r < len(s2):
        while j < size:
            hash2[s2[l]] = hash2.get(s2[l], 0) + 1
            j+=1
            l+=1
        if hash1 == hash2:
            return True
        
        hash2[s2[l-size]] -=1
        if hash2[s2[l-size]] == 0:
            del hash2[s2[l-size]]
        j-=1
        r+=1
    
    return False


print(solve("ab", "eidbaooo"))

'''
seems like just make a sliding window the size of s1, then see if the chars of s1 are in s2 and if so we are done

i tried for like 20 mins and i couldnt do it BUTTTT I ACC DID ITTT YAYYY!! using that solution above ^^. i was just messing up the "l-size" i was doing "l-1". and then i realized i was doing a for r in range(len(s2)) but l was going faster than r so it didnt work. i almost gave up but didnt and it worked

some notes after sol: the [l-size] basically just deletes the furthest left char and we always add the furtherest right char in the window. noticing this r does nothing in this case since its all done with l. however i think i could remove the first while statment with 'l' and replace it with 'r' and then just keep the 'l' for the 'l-size', ie i wouldnt have to do 'l-size' i could just do 'l'
'''