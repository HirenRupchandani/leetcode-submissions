class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hmap = {}
        distincts = []
        for n in arr:
            hmap[n] = hmap.get(n, 0) + 1
        for key,value in hmap.items():
            if value == 1:
                distincts.append(key)
        # print(distincts)
        if len(distincts) >= k:
            return distincts[k-1]
        return ""

        