class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set left part of window
        left = 0
        # Set max length
        maxLength = 0
        # Initialize a set
        charSet = set()
        # Set right part of window:
        for right in range(len(s)):
            # If the current character is found in charSet
            while s[right] in charSet:
                # Remove all the characters till the repeated character is removed
                charSet.remove(s[left])
                # Shift the window to left to skip the duplicates
                left+=1
            # Add the current character to the charSet
            charSet.add(s[right])
            # Compare the new substring length with previous maxLength
            maxLength = max(maxLength, right-left+1)
        return maxLength
