class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        result = 0
        importances = {}
        for src, dst in roads:
            importances[src] = importances.get(src, 0) + 1
            importances[dst] = importances.get(dst, 0) + 1
        importances = dict(sorted(importances.items(), key=lambda item: item[1], reverse=True))
        importances = {k:n-i for i,k in enumerate(importances.keys())}
        # print(importance)
        for src, dst in roads:
            result += importances[src] + importances[dst]
        return result