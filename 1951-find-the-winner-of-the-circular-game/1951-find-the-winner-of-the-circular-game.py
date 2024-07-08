class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        l = [i+1 for i in range(n)]
        while len(l) > 1:
            i = (i + k - 1) % len(l)
            l.pop(i)
        return l[0]