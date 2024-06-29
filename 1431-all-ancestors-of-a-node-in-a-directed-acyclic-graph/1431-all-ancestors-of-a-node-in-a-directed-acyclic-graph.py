class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # contruct a graph from children to parent
        graph = defaultdict(list)
        for a, b in edges:
            graph[b].append(a)
        
        result = []
        # For each node
        for i in range(n):
            # Put the node in a queue
            queue = deque([i])
            visited = set()
            # Append the neighbors in queue while queue is not empty and append neighbors in visited
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            # Append the visited nodes into result
            result.append(sorted(list(visited)))
        return result

        # My Solution: 79/80 ran with one TLE
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