class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag = False
        flagCounter = 0
        for number in arr:
            if number%2 == 0:
                flag = False
                flagCounter = 0

            else:
                flag = True
                flagCounter += 1
                if flagCounter == 3:
                    return True
        return False
        