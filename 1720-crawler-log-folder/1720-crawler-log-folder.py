import re
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0 # main
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if count > 0:
                    count -= 1
            else:
                count += 1
        return count
                
        stack = ["main"]
        # Pattern to find folder name
        pattern = r'([a-zA-Z0-9]+)/'
        for log in logs:
            # To stay in same folder
            if log == "./":
                continue
            # To go back (pop the stack head)
            elif log == "../":
                if stack[-1] != "main":
                    stack.pop()
            # Find and insert folder name in stack
            else:
                # Search for the pattern in the input string
                match = re.search(pattern, log)
                # Check if there is a match
                if match:
                    # Extract the matched group
                    stack.append(match.group(1))
        return len(stack) - 1