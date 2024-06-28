class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        def sort_key(key):
            # print(len(key[1]))
            return len(key)
        imp = {}
        for src, dst in roads:
            imp[src] = imp.get(src, 0) + 1
            imp[dst] = imp.get(dst, 0) + 1
        # print(imp)
        
        imps = dict(sorted(imp.items(), key=lambda item: item[1], reverse=True))

        # print(imps)
        result = 0
        importances = {k:n-i for i,k in enumerate(imps.keys())}
        # print(importances)
        for src, dst in roads:
            # print(src, dst, importances[src] + importances[dst])
            result += importances[src] + importances[dst]

        return result