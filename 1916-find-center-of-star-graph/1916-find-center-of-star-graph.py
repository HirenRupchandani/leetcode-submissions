class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
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