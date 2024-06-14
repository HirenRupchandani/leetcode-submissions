class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        count = 0
        prev = nums[0]
        for num in nums[1:]:
            if num <= prev:
                prev += 1
                count += prev - num
            else:
                prev = num
        return count