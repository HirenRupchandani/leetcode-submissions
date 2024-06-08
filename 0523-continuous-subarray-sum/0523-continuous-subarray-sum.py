class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # A hashmap
        map = {0:-1}
        sum = 0
        for i in range(len(nums)):
            # Calculate cumulative sum of each element
            sum += nums[i]
            # Get remainder of the current sum
            rem = sum % k
            # If that remainder already exists in the map
            if rem in map:
                # and the (previous stored index - current index) > 1
                if i-map[rem] > 1:
                    # Subarray exists
                    return True
            else:
                # Else just update the remainder as key and the index as value in the map
                map[rem] = i
        # Return False if the conditions fail
        return False
        