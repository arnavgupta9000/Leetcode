#Given a binary tree, determine if it is height-balanced
#Height-Balanced: A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one..

def solve(root):
    
    def dfs(tree):
        if not tree:
            return [True, 0] # if the node is empty its balanced and with a height of 0
        
        left, right = dfs(tree.left), dfs(tree.right) # recursive call 

        balance = (abs(left[1] - right[1]) <= 1 and left[0] and right[0]) # if both left and right subtrees are balanced and the height of abs(left subtree - left subtree) <= 1 it is still balanced

        return [balance, 1 + max(left[1], right[1])] # are we balanced? and the height of the current subtree 
    
    return dfs(root)[0]