class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Parent of each node
        par = [i for i in range(len(edges) + 1)]
        
        # Rank of each node -> More children = More Rank
        rank = [1] * (len(edges) + 1)

        # Check the parent (ancestor) of the node 
        def find(n):
            p = par[n]
            while p!=par[p]:
                # Jumping to grandparent -> Path Compression
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            # Check between parents of n1, and n2
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p2] += 1
            else:
                par[p1] = p2
                rank[p1] += 1
           
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]