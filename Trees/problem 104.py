# max depth of binary tree

def dfs(tree):
    if not tree:
        return 0  # max depth of nothing is 0         
    return 1 + max(dfs(tree.left), dfs(tree.right)) # get the max of right subtree and left subtree. +1 since the root node(tree) is the node we are on so therefore we should just add 1 to it