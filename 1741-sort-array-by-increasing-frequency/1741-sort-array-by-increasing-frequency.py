class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(NlogN), Space: O(N^2) [worst for nested values]
        result = []
        hmap = {}
        h2 = {}
        # Get a normal hashmap
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        # print(hmap)
        # Convert the hashmap to value, key pairs where keys are in a list
        for k,v in hmap.items():
            if v not in h2:
                h2[v] = []
            h2[v].append(k)
        # print(h2)
        # Sort the keys (frequencies)
        h2 = dict(sorted(h2.items()))
        # print("sorted", h2)

        # For each k, v pair
        for k, v in h2.items():
            # Check for multiple values
            if len(v) > 1:
                # If yes, sort the list in descending order
                v.sort(reverse=True)
                # Parse every value and add to the result k times
                for i in range(len(v)):
                    result += [v[i]]*k
            else:
                # Else just add the value k times
                result += [v[0]]*k
        # print(result)
        return result