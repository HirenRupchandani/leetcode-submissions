class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0 or c == 1:
            return True
        x = int(c ** (1/2))
        arr = [i*i for i in range(1, x+1)]
        l = 0
        r = x-1
        while l<=r:
            if arr[r] == c or arr[l] == c:
                return True
            if arr[r] + arr[l] == c:
                return True
            elif arr[r] + arr[l] < c:
                l+=1
            else:
                r-=1
        return False