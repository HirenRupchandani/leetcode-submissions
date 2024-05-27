class Solution:
    def specialArray(self, nums: List[int]) -> int:
        result = -1
        d = {}
        maxi = max(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         print(nums[i], nums[j])
        #         if nums[i]>=nums[j]:
        #             d[nums[i]] = d.get(nums[i],0) + 1
        for i in range(maxi+1):
            for j in range(len(nums)):
                # print(i, nums[j])
                if i<=nums[j]:
                    d[i] = d.get(i,0) + 1
        # print(d)

        for key, value in d.items():
            if key==value:
                return key
        return -1

        