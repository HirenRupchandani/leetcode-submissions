class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort() - > LoL
        result = []
        l = [0,0,0]
        for num in nums:
            l[num] += 1
        for i in range(3):
            result += [i] * l[i]
        # print(result)
        nums[:] = result[:]
