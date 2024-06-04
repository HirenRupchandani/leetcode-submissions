class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}
        odd = 0
        res = 0
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
        for k,v in hmap.items():
            # print(k, v)
            if v%2 == 0:
                print(k, v)
                res += v
            if v%2 != 0:
                odd = 1
                res += v-1
        return res + 1 if odd else res
        