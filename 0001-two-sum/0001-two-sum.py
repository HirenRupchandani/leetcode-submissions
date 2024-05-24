class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary
        values= {}
        # Use enumeration to traverse the input
        for index, num in enumerate(nums):
            # Calculate difference
            diff = target - num
            # If difference is a key in the dictionary:
            if diff in values:
                # Return indices as values
                return [index, values[diff]]
            # If false, set the (key, value) pair as (input_value, index)
            values[num] = index