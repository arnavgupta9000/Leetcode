#Given the root of a binary tree, determine if it is a valid binary search tree (BST).

#A valid BST is defined as follows: The left subtreeof a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

def solve(root):
    def dfs(tree, left, right, left_v, right_v):
        if not tree:
            return True
        if not left and not right: # to start the search at the root node
            return dfs(tree.left, True, False, tree.val, False) and dfs(tree.right, False, True, False, tree.val)
        
        if left:
            # nodes that are smaller
            if tree.val <= left_v: # valid
                return dfs(tree.left, True, False, tree.val, False)
            return False # its not valid
        if right:
            if tree.val >= right_v:
                return dfs(tree.right, False, True, False, tree.val)
            return False
    
    return dfs(root, None, None, 0, 0)

def solve2(root):

    def valid(node, left, right):
        if not node:
            return True
        
        if not(left < node.val < right):
            return False
        
        return valid(node.left, left, node.val) and valid(node.right, node.val, right) # left subtree = less than the parent
    return valid(root, -float('inf'), float('inf'))
        


'''
thinking we just need to run a dfs where we have 2 extra params telling us if its a right or left, and tracking the max value of right/left
problem with [5,4,6,null,null,3,7] ie we have

                    5
                4        6
                      3     7
this should return false since theres a 3 on the left side of the 5 but my algo orginally doesnt take care of that

i couldnt solve it on my own in the end..
'''

