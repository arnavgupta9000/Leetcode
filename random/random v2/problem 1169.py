'''
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

'''

# however this is an O(n^2) time. the O(nlogn is as follows)

from collections import deque
from typing import List

def solve( transactions: List[str]) -> List[str]:
    if not transactions:
        return []
    
    transactions.sort(key=lambda x: int(x.split(",")[1]))  # Sort by time
    
    res = set()
    names = {}

    for i, transaction in enumerate(transactions):
        name, time, cost, city = transaction.split(",")
        time, cost = int(time), int(cost)

        if cost > 1000:
            res.add(transaction)

        if name not in names:
            names[name] = deque()

        # Remove transactions older than 60 minutes
        while names[name] and time - names[name][0][0] >= 60:
            names[name].popleft()

        # Check all remaining transactions (only recent ones)
        for prev_time, prev_city, prev_tx in names[name]:
            if city != prev_city:
                res.add(transaction)
                res.add(prev_tx)

        # Add current transaction to deque
        names[name].append((time, city, transaction))

    return list(res)

print(solve(["alice,20,800,mtv","bob,50,1200,mtv"]))

'''
couldnt solve on my own altho after i failed the first few times i knew what was wrong but to lazy to correct it
'''