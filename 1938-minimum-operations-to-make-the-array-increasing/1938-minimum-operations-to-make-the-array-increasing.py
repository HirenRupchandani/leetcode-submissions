class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        count = prev = 0
        for num in nums:
            if num <= prev:
                prev += 1
                count += prev - num
            else:
                prev = num
        return count