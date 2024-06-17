class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = int(c ** (1/2))
        # arr = [i*i for i in range(1, x+1)]
        l = 0
        r = x
        while l<=r:
            y = l**2 + r**2
            if y==c:
                return True
            if y<c:
                l+=1
            else:
                r-=1
        return False