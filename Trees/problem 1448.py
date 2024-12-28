#Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

#Return the number of good nodes in the binary tree.

class Tree:
    def solve(self, root):
        self.res = 0
        def dfs(tree, c):
            if not tree:
                return 0
            c = max(c, tree.val)
            if tree.val >= c:
                self.res +=1
            dfs(tree.left, c)
            dfs(tree.right, c)

            
            
        dfs(root, -float('inf'))
        return self.res

    def solve2(root):

        def dfs(tree, val):
            if not tree:
                return 0

            res = 1 if tree.val >= val else 0
            val = max(val, tree.val)
            res += dfs(tree.left, val) + dfs(tree.right, val)
            return res
        return dfs(root, root.val)
    


'''
had to look at the hints on neetcode websites but i did solve it on my own. its not to hard once you know what ur doing

solution 2 is using a non global var
'''