#Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


class Tree:

    def solve(self, root,k):

        def dfs(tree):
            if not tree:
                return 
            
            dfs(tree.left)
            self.k-=1
            if self.k == 0:
                self.k = -1 # so k cannot be updated again after a value is found
                self.res = tree.val
                return

            dfs(tree.right, self.k)

            return


        self.res = 0
        self.k = k
        dfs(root)
        return self.res

def solve2(root, k):
    n = 0 # once n == k then thats the element we want
    stack = []
    curr = root
    '''
    If only curr was used:

The loop would terminate as soon as we hit a None node (i.e., the end of a left subtree).
This would skip all nodes stored in the stack, preventing the algorithm from backtracking to process higher-level nodes or their right subtrees.

If only stack was used:
The loop would fail to start if curr was not initialized to the root.
It would also fail to explore deeper nodes when moving to the left or right because curr is responsible for moving down the tree.
    '''

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop() # pop most recent item
        n+=1
        if n == k:
            return curr.val
        curr = curr.right
    return 0


            
        

'''
first idea, go through every node and make it into a list, and then sort, but this is O(nlogn).

so instead we know its a bst we're gonna try to follow the bst property and findt he kth smallest value

ok so i got it, but not sure why this even works... like i get why but its super weird (and took a lot of trial and error) so still gonna watch the vid and try it that way

'''