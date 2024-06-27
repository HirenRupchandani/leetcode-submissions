class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Pythonic solution in discussion:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]
        # A classic solution
        nodes = {}
        maxEdges = 0
        result = -1
        for src, dst in edges:
            nodes[src] = nodes.get(src, 0) + 1
            nodes[dst] = nodes.get(dst, 0) + 1
        for node in nodes: 
            if nodes[node] > maxEdges:
                result = node
                maxEdges = nodes[node]
        return result