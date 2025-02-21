# invert binary tree

# given that we have the root -> run a dfs but swap the elements
def dfs(root):
    if not root: # base case
        return None
    root.left, root.right = root.right, root.left # this is where the swapping occurs
    dfs(root.left) # go the left child and keep swapping
    dfs(root.right)
# if were at a leaf node we do get None, None = None, None

'''
def dfs(tree):
    if not tree:
        return None
    tree.left, tree.right = dfs(tree.right), dfs(tree.left)
    return tree

    return dfs(root)

this also works. notice the return tree this time since we arent changing the links themselves.

Exactly! The key difference is that instead of returning None when we reach a leaf node, we now return the leaf node itself. This ensures that when the recursion unwinds, the returned leaf nodes are swapped correctly at their parent level.
'''