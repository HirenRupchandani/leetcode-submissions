class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time<n:
            return time+1
        pillow = 1
        direction = 1
        while time:
            if pillow == n:
                direction = -1
            elif pillow == 1:
                direction = 1
            pillow += direction
            time -= 1
        return pillow 

            

        