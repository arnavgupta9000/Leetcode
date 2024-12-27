#Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

import collections

def solve(root):
    if not root:
        return []
    res = []
    q = collections.deque()
    q.append(root)

    while q:
        level = []

        for _ in range(len(q)): # this will tell us how many nodes are at the specific level and popleft() will remove the left one but the len(q) for the for loop doesnt change hence why this works. ie think of it like how many elemnts are in the queue at this point. then we just delete all of them while adding the children
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        res.append(level)
    return res




'''
clearly its just a bfs but idk how that works so now is a good time to learn...

'''