class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        result = 0
        a,b = 'ab', 'ba'
        if y>x:
            b,a,y,x = a,b,x,y
        
        for word in [a,b]:
            stack = []
            i=0
            while i<len(s):
                stack.append(s[i])
                n = len(stack)

                prefix = stack[n-2] + stack[n-1]
                # if see the prefix ab or ba move from stack and increment the answer
                if prefix == word:
                    result += x
                    stack.pop()
                    stack.pop()
                i+=1
                # change the x point to y for 2nd iteration
            x=y
            # assign new letters with already removed prefix
            s=''.join(stack)
        return result 