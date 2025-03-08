'''
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].
'''
import math

def solve(left, right):
    def get_primes():
        # sieve of eratosthenes algo
        # the time for this algo is O(n log(log(n)))
        ''' - find which numbers are NOT prime
        basically say u have a range of 0-10 so make an array of size 10 and set everything to true
        then set 0=F, 1=F. then starting from 2 u say ok 2 if prime, but then every mutiple isnt, ie 4,6,8,10 are all not prime. then since 3 hasnt been visited it, it is prime, but 6,9 are not. since 4 is already marked prime, skip iteration. etc

        can stop at sqrt(n) since every number after is already covered 
        '''

        is_prime = [True] * (right + 1) # want to include right + 1 spot
        is_prime[0] = is_prime[1] = False

        for n in range(2, int(math.sqrt(right)) + 1): # +1 to be inclsuive
            if not is_prime[n]:
                continue
            for m in range(n + n, right + 1, n): # start atn+n, increments of n
                is_prime[m] = False
        
        primes = []

        for i in range(len(is_prime)):
            if is_prime[i] and i>= left: # since we start at 0
                primes.append(i)
        return primes

        
    primes = get_primes() # all primes from [left, right]

    res = [-1, -1]
    diff = float("inf")

    for i in range(1, len(primes)):
        if primes[i] - primes[i-1] < diff:
            diff = primes[i] - primes[i-1]
            res = [primes[i-1], primes[i]] # smaller number first
    return res

print(solve(left = 10, right = 19))

'''
med

watched vid...

the not getting prime numbers part (everything else) is linear since u only need to scan once since you know the min distance is the elements next you (since the array is sorted) ie [15, 17, 19], 15 only needs to look at 17 since 17 will be closer to 15 than anything after it
'''