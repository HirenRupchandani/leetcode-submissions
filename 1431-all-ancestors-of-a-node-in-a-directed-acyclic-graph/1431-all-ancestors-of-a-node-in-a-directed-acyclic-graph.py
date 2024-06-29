class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[b].append(a)
        
        ans = []
        for i in range(n):
            queue = deque([i])
            visited = set()
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            ans.append(sorted(list(visited)))
        return ans
        connected = {}
        for u, v in edges:
            if v in connected:
                connected[v].add(u)
            else:
                connected[v] = {u}
            # connected[v] = connected.get(v, []) + [u]
        for k, v in connected.items():
            visited = [0 for _ in range(n)]
            nodes = v.copy()
            for node in nodes:
                if node in connected and not visited[node]:
                    v.update(connected[node])
                visited[node] = 1
            connected[k] = sorted(list(v))
        result = []
        for i in range(n):
            if i not in connected:
                result.append([])
            else:
                result.append(list(connected[i]))
        return result