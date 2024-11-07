class Solution:
    def isValid(self, s: str) -> bool:
        # dict with close:open bracket as k:v pairs
        paranthesis = {"}":"{", ")":"(", "]":"["}
        # stack as an empty list
        stack = []
        # For each bracket
        for c in s:
            # If it is a open bracket, push to stack
            # if c is [ or { or (
            if c not in paranthesis.keys():
                stack.append(c)
                continue
            # For a closed bracket:
            # If stack is empty or top of stack (should be a corresponding open bracket) doesn't match the corresponding key's value: return False
            if len(stack)==0 or stack[-1]!=paranthesis[c]:
                return False
            # simply pop if closed bracket and open bracket match
            stack.pop()
        # If stack empty, return True, else False
        return not stack