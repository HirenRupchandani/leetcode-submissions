class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = 0
        for number in arr:
            if number%2 == 0:
                odds = 0
            else:
                odds += 1
                if odds == 3:
                    return True
        return False
        