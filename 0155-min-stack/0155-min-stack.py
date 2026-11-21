class MinStack:

    def __init__(self):
        self.s = []
        self.min = 2**31
        self.lastMin = []
    def push(self, value: int) -> None:
        if value <= self.min:
            self.lastMin.append(self.min)
            self.min = value
        self.s.append(value)
    def pop(self) -> None:
        rem = self.s.pop()
        if rem == self.getMin():
            self.min = self.lastMin.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()