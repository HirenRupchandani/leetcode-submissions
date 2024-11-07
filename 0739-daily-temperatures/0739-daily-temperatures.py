class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        days = len(temperatures)-1
        for temp in temperatures[-1::-1]:
            # print('stack:', stack)
            # print(temp, days)
            # if not stack:
            #     # print('empty stack, pushing 0')
            #     result.append(0)
            #     stack.append((temp, days))
            #     days-=1
            #     continue
            # print(temp, stack[-1][0], temp >= stack[-1][0])
            while stack and temp >= stack[-1][0]:
                topTemp, topDay = stack.pop()
                # print('popped val:', topTemp, topDay)
            
            if stack:
                # print('result val:', stack[-1][1] - days)
                result.append(stack[-1][1] - days)
                stack.append((temp, days))
            else:
                result.append(0)
                stack.append((temp, days))
            days-=1
        # print(result[-1::-1])
        return result[-1::-1]