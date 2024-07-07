class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles:
            numBottles, rem = numBottles // numExchange, numBottles % numExchange
            result += numBottles
            numBottles += rem
            if numBottles < numExchange:
                break
        return result

        