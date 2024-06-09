class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        Hmap = {0:1}
        prefix = 0
        for i in range(len(nums)):
            # print(nums[i])
            prefix = (prefix + nums[i]) % k
            res += Hmap.get(prefix, 0)
            Hmap[prefix] = Hmap.get(prefix, 0) + 1
            
        # print(Hmap)
        return res