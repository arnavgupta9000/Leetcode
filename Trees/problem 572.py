#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

def solve(s, t):

    if not t:
        return True
    
    if not s: # s is empty and t is non emtpy. clearly then t is not a subtree of s
        return False

    if same_tree(s, t):
        return True
    if solve(s.left,t) or solve(s.right,t):
        return True
    return False

def same_tree(s, t):
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return same_tree(s.left, t.left) and same_tree(s.right, t.right)
        
        return False # if not tree has something and another one doesnt... end returns false


'''
Why this works? basically your calling same tree on every node of the tree. which in hindsight is super obvious but...

'''