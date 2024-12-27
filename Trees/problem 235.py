#Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

def solve(root, p, q):
    curr = root

    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.left
        else:
            return curr


'''
no clue on where to even begin...

so after watching video explanation (without the coding part) we notice thats its a bst which helps our search. we also notice that if a node is the ancestor than that is the LCA... ok i still have no idea what to do...

ok so the solution is pretty easy once u know what ur doing. ie since its a bst we know that right subtree = greater, left subtree = smaller. but we also know this: if p is on one side and q is on another side, then the LCA must be the node where we currently are. if they are both greater then go to the right tree, else go the left tree.
'''