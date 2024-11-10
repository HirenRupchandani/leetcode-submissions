class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack
        stack = []
        maxArea = 0
        # Idea is to check the increasing order of heights
        # We have to see how much we can extend the intial height of the order/sequence
        # Store the heights and indices of those elements
        # Whose height breaks the increasing order of heights
        
        for i, h in enumerate(heights):
            # Set a start index whose index can stretched as far as possible
            start = i
            # If a height breaks the sequence i.e. it is smaller than height in stack
            while stack and stack[-1][1] > h:
                # Keep popping the larger heights from stack
                index, height = stack.pop()
                # Calculate the max area between the popped height and current index
                maxArea = max(maxArea, height * (i - index))
                # Set the start index (which is smaller index of a previous small height) to the popped height to extend it ahead
                start = index
            

            # Append the current height with the start index
            stack.append((start, h))
        
        # After the parsing is done, we need to calculate the heights that are extended till the end.
        for i, h in stack:
            # Height * (End_Index - Index stored in stack)
            maxArea = max(maxArea, h * (len(heights) - i))
        
        # Return max height
        return maxArea

        