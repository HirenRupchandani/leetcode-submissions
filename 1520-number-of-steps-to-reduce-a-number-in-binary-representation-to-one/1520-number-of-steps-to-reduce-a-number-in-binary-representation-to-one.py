class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        n = len(s)
        steps = 0
        for i in range(n-1, -1, -1):
            num += int(s[i]) * 2 ** (n-i-1)
        print(num)
        while num>1:
            if num%2==1:
                num += 1
            else:
                num = num // 2
            steps += 1
        return steps
        # return num//2

        