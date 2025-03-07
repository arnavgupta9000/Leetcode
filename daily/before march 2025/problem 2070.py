#You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

#You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

#Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

def solve(items, queries):
    items = sorted(items, key=lambda l:l[0])        
    # can also just do items.sort()

    queries = sorted([(q, i) for i, q in enumerate(queries)])

    max_bea = 0
    j=0
    res = [0] * len(queries)

    for q, i in queries:
        while j < len(items) and items[j][0] <= q:
            max_bea = max(max_bea, items[j][1])
            j+=1
        res[i] = max_bea # it needs to be like this since the query order now might be different, but
        # since we stored the original query index in i in queries, we can now do res[i] = value
    return res

print(solve([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6]))

'''
Video: we basically sort both lists. but to sort the queries list, we need to save the original index of the query[i] since thats the ith position in result. then once that is done we can just start going though all items. once a lower price is eliminated, we move the j pointer up keeping track of the max beauty as that will be the lowest for all queries with a higher price.
'''