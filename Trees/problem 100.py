#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

def solve(p, q):
    def dfs(tree,arr):
        if not tree:
            arr.append(None)
            return
        
        dfs(tree.left, arr)
        dfs(tree.right, arr)

        arr.append(tree.val)
        return arr
    
    return dfs(p, []) == dfs(q,[])


def solve1(p,q):
    
    if not p and not q: # both are not null
        return True
    
    if not p or not q: # 1 is not null, since if both were null the above if statement would take care of it
        return False
    
    if p.val != q.val:
        return False
    return solve(p.left, q.left) and solve(p.right, q.right) # we want both to be true

    


'''
Intution: just make an array, and see if the arrays are equal to each other. worked (without ANY help), time = O(n), space = O(n+m)

But there is another way that uses much less space and is way more obvious and cleaner, idk how i missed it solve1()
'''