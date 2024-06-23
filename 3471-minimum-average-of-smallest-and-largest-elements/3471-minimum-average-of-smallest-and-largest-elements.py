class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        n = len(nums)//2
        while nums and n:
            n -= 1
            mini = nums.pop(0)
            maxi = nums.pop(-1)
            avg = (mini+maxi)/2
            averages.append(avg)
        print(averages)
        return min(averages)
