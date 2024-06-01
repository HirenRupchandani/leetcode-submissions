class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        diff = 0
        for i in range(1, n):
            diff += abs(ord(s[i]) - ord(s[i-1]))
        return diff