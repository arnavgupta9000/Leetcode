'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.'''

def solve(node):
    def Node(): # to avoid seeing the errors
        pass
    hash = {}
    def dfs(node):
        if node in hash:
            return hash[node]
        
        copy = Node(node.val)
        hash[node] = copy
        for n in node.neighbhors:
            copy.neighbhors.append(dfs(n))
        return copy
    
    return dfs(node) if node else None

  

'''
just watched a vid, my graph understanding atp still isnt the best

ok so thing to take away is that the input lists is the index ie [[2,4],[1,3],[2,4],[1,3]]. the [2,4] represents node 1 (index + 1) and is connected to nodes 2,4. [1,3] is node 2 and its connected to 1 and 3
'''