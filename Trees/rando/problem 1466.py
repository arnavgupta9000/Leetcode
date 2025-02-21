'''
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
'''

class graph:
    def solve(self, n, connections):
        graph = [[] for _ in range(n)]
        edges = set()

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            # these 2 lines make it an undirected graph
            edges.add((u,v)) # keep the og connection (1 way)

        visited = set()
        self.res = 0
        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if (node, neighbor) in edges:
                    self.res +=1
                dfs(neighbor, node)

        
        dfs(0, -1) # start the dfs at node 0, it has no parents
        return self.res

'''
But since a tree has no cycles, and we prevent revisiting using parent, DFS never visits a node more than once.

the reason why the dfs call is inside the for loop is cause there its a tree so each node can only have 1 parent
'''