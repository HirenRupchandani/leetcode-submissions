class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = {}
        result = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for num in counter.keys():
            if counter[num] == 1:
                result.append(num)
        return result