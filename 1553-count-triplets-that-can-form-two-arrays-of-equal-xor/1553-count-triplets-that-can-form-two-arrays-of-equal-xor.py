class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)  # Length of the array
        prefix = [0] * (n + 1)  # Initialize prefix XOR array with an extra zero for ease of computation
        
        # Compute the prefix XOR from the beginning up to each index
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        ans = 0  # Initialize the answer count to 0
        
        # We use a dictionary to keep track of how many times each prefix XOR value has occurred
        # and the indices at which each XOR value has occurred
        count = {}
        
        # Loop through each possible prefix XOR value
        for k in range(n + 1):
            if prefix[k] in count:
                # If the current prefix XOR has been seen before, iterate through the indices
                # where this XOR value has occurred before
                for (i, total) in count[prefix[k]]:
                    # For each index 'i' that we've seen this prefix XOR, calculate the number of j's
                    # There are (k - 1 - i) possible values of j for each i (from i+1 to k-1)
                    ans += (k - 1 - i) * total
            # Add/update the current prefix XOR in the dictionary
            # If it's not in the dictionary, add it with current index and count as 1
            if prefix[k] not in count:
                count[prefix[k]] = []
            # Append the current index and 1 to the list for this XOR value
            # We keep appending to track all indices where this XOR occurs and the count
            count[prefix[k]].append((k, 1))
        
        return ans  # Return the computed number of triplets