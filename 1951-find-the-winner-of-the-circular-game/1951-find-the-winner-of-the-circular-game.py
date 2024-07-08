class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Recursion With Subproblems
        def recursion(n, k):
            if n==1:
                return 0
            return (recursion(n-1, k) + k) % n
        return recursion(n, k) + 1
        
        # Simulation -> My Solution
        i = 0
        l = [i+1 for i in range(n)]
        while len(l) > 1:
            i = (i + k - 1) % len(l)
            l.pop(i)
        return l[0]