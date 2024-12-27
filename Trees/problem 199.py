#Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

import collections
def solve(root):
    if not root:
        return []
    res = []
    que = collections.deque()
    que.append(root)

    while que:
        level = []
        for _ in range(len(que)):
            node = que.popleft()

            level.append(node.val)

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        res.append(level[-1])
    return res
            
        


'''
idea seems to be just use a bfs and only append the RIGHT most value. can do this by storing every value in a list and then just taking the last value of that level

worked on my own
'''