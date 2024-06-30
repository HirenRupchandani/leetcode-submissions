class UnionFind:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * (n+1)
        self.parent = parA = [i for i in range(n+1)]
    def find(self, x):
        while x!=self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 0
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        # If union is performed, reduce the number of components by 1
        self.n -= 1
        return 1
    
    def is_connected(self):
        # Making sure the graph is unionized and not disjoint
        print(self.n)
        return self.n == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Edges - # of edges added = Result
        connected = 0
        alice, bob = UnionFind(n), UnionFind(n)

        for typ, src, dst in edges:
            if typ == 3:
                connected += (alice.union(src, dst) | bob.union(src, dst))

        for typ, src, dst in edges:
            if typ == 1:
                connected += alice.union(src, dst)
            elif typ == 2:
                connected += bob.union(src, dst)
        print(bob.is_connected(), alice.is_connected())
        if bob.is_connected() and alice.is_connected():
            return len(edges) - connected

        return -1