class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Josephus problem -> T: O(n), S: O(1)
        index = 0
        for i in range(1, n+1):
            index = (index + k) % i
        return index + 1

        # Recursion With Subproblems -> T: O(n), S: O(n)
        def recursion(n, k):
            if n==1:
                return 0
            return (recursion(n-1, k) + k) % n
        return recursion(n, k) + 1
        
        # Simulation -> My Solution -> T: O(n^2), S: O(n)
        i = 0
        l = [i+1 for i in range(n)]
        while len(l) > 1:
            i = (i + k - 1) % len(l)
            l.pop(i)
        return l[0]