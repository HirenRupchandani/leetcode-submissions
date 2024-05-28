class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        res = 0
        n = len(s)
        start = 0
        cost = 0
        for end in range(n):
            # Check the cost at this index
            cost += abs(ord(s[end]) - ord(t[end]))

            # Slide the window and decrease cost till it replinishes maxCost
            while cost > maxCost:
                cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            
            res = max(res, end - start + 1)

        return res