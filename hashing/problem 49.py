#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

def solve(strs):
    
    hash = {}
 
    for i in strs:
        hash2 = []
        for j in i:
            hash2.append(j)
        hash2.sort()
        if "".join(hash2) in hash:
            hash[ "".join(hash2) ].append(i)
        else:
            hash[ "".join(hash2) ] = [i]
    # print(hash)
    res = []
    for value in hash.values():
        res.append(value)
        
    return res 

# a more efficient solution for the first solve
'''
    for i in strs:
        sorted_word = ''.join(sorted(i)) 
        if sorted_word in hash:
            hash[sorted_word].append(i)
        else:
            hash[sorted_word] = [i]

When sorted('ant') is called:
The string 'ant' is treated as an iterable of characters: ['a', 'n', 't'].
These characters are then sorted. Since 'ant' is already sorted alphabetically, the output is ['a', 'n', 't'].
'''

def solve2(strs):
    hash = {}

    for i in strs:
        count = [0] * 26 # create an array count of size 26, initialized to 0. Each index represents a letter in the alphabet (a-z)


        for c in i:
            count[ord(c) - ord('a')] +=1 #ord(c) - ord('a') converts the character into its alphabetical index (e.g., 'a' -> 0, 'b' -> 1, etc.).

        
        key = tuple(count) #The count list is converted to a tuple so it can be used as a dictionary key. Tuples are immutable and hashable, unlike lists.

        if key in hash:
            hash[key].append(i)
        else:
            hash[key] = [i]
    print(hash)
    '''
    res = []
    for value in hash.values():
        res.append(value)
        
    return res
    '''
    return list(hash.values()) # this is used instead of ^^, however both work

def solve3(strs):
    freq = {}
    for i in strs:
        word = "".join(sorted(i))
        if word in freq:
            freq[word].append(i)
        else:
            freq[word] = [i]
    
    return list(freq.values())


        

print(solve(["eat","tea","tan","ate","nat","bat"]))


'''
use anograms but sort the lists we use to then output the result. done on my own. had a few problems mainly the fact that i was trying to manually format the string ie on the
hash[ "".join(hash2) ].append(i) line i was doing += f'i ' instead of the append. notice this is not the most optimal due to the sort it has an additional log factor in the time complexity however still passes all leetcode casses

the better solution is the most optimal
'''