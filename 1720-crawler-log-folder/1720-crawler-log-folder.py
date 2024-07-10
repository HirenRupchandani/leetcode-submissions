import re
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = ["main"]
        pattern = r'([a-zA-Z0-9]+)/'
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if stack[-1] != "main":
                    stack.pop()
            else:
                # Search for the pattern in the input string
                match = re.search(pattern, log)
                # Check if there is a match
                if match:
                    # Extract the matched group
                    stack.append(match.group(1))
        return len(stack) - 1