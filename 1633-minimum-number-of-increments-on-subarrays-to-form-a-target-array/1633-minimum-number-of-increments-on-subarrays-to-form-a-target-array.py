class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = prev = 0

        for v in target:
            if v > prev:
                res += (v - prev)
            prev = v
        return res