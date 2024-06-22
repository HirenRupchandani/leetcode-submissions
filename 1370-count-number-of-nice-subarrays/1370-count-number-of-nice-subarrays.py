class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hmap = {0:1}
        odd = 0
        result = 0
        for i, num in enumerate(nums):
            # If odd, increase counter
            if num%2 != 0:
                odd += 1
            # If odd-k is in hmap means we have a subarray with some count of odd numbers atleast equal to k
            if odd - k in hmap:
                # Add those numbers to the current result
                result += hmap[odd-k]
            # Update the current odd count in the hmap for future passes
            hmap[odd] = hmap.get(odd, 0) + 1
        return result