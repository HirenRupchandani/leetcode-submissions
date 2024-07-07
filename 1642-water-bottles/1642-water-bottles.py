class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Time & space: O(1) -> Better Solution (Geometric Sum)
        return numBottles + (numBottles - 1) // (numExchange - 1)


        # Time: O(log(numBottles)), space: O(1) -> My solution
        result = numBottles
        while numBottles >= numExchange:
            numBottles, rem = numBottles // numExchange, numBottles % numExchange
            result += numBottles
            numBottles += rem
        return result

        