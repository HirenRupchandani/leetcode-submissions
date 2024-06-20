class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        # To check whether or not m balls could be distributed into the baskets 
        def feasible(force: int) -> bool:
            x, k = 0, m
            for i in range(len(position)):
                if position[i] >= x:
                    x, k = position[i] + force, k - 1
                    if k == 0:
                        return True
            return False
        l, r = 1, (position[-1] - position[0]) # max - min
        # When breaking the loop, l will be the maximal number satisfying the feasible function;
        # It means that l is the answer.
        while l<r:
            mid = l + (r-l+1) // 2
            if feasible(mid):
                l = mid
            else:
                r = mid - 1
        return l




        
        