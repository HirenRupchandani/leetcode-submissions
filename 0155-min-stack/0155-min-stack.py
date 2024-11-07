class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMin = float('inf')
        self.topStack = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stackMin = min(self.stackMin, val)
        self.topStack = val

    def pop(self) -> None:
        val = self.stack.pop()
        if self.stack:
            self.stackMin = min(self.stack)
            self.topStack = self.stack[-1]
        else:
            self.stackMin = float('inf')
        return val

    def top(self) -> int:
        return self.topStack

    def getMin(self) -> int:
        return self.stackMin

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()