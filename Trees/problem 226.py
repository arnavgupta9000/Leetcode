# invert binary tree

# given that we have the root -> run a dfs but swap the elements
def dfs(root):
    if not root: # base case
        return None
    root.left, root.right = root.right, root.left # this is where the swapping occurs
    dfs(root.left) # go the left child and keep swapping
    dfs(root.right)
# if were at a leaf node we do get None, None = None, None