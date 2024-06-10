class Solution:
    # From the editorial:
    def counting_sort(self, arr):
        # Create the counting hash map.
        counts = {}
        # Find the minimum and maximum values in the array.
        min_val, max_val = min(arr), max(arr)

        # Update element's count in the hash map.
        for val in arr:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1

        index = 0
        # Place each element in its correct position in the array.
        for val in range(min_val, max_val + 1):
            # Append all 'val's together if they exist.
            while counts.get(val, 0) > 0:
                arr[index] = val
                index += 1
                counts[val] -= 1

    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        # expected = sorted(heights)
        expected = heights[:]
        self.counting_sort(expected)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result += 1
        return result