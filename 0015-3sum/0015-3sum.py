class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # For each element
        for i, a in enumerate(nums):
            # If next element is same, continue
            if i>0 and a == nums[i-1]:
                continue
            
            # Set L and R as next element and last element
            l, r = i+1, len(nums) - 1

            # While L<R:
            while l<r:
                # Calculate the sum of 3 numbers
                threeSum = a + nums[l] + nums[r]
                # If sum>0, decrement right by 1
                if threeSum > 0:
                    r -= 1
                # If sum<0, increment left by 1
                elif threeSum < 0:
                    l += 1
                # If sum=0, append result
                else:
                    res.append([a, nums[l], nums[r]])
                    # l and r will be updated regularly on above conditions
                    # set new value of l and continue
                    l += 1
                    # Incase new L and old L are same, increment by 1 again
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res