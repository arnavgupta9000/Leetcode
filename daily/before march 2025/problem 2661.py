def solve(arr, mat):
    hash = {}
    
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            hash[str(i)] = hash.get(str(i), 0) + 1
    # return hash

    for i in range(len(arr)):
        hash[i]

print(solve([1,3,4,2], [[1,4],[2,3]]))