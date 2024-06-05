class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        hMap = {}
        for c in words[0]:
            hMap[c] = hMap.get(c, 0) + 1 
        for x in hMap:
            for i in range(1, len(words)):
                if x in words[i]:
                    hMap[x] = min(hMap[x], words[i].count(x))
                else:
                    hMap[x] = 0
        for key, value in hMap.items():
            res += value * [key]
        return res
                