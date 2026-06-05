class MinStack:

    def __init__(self):
        self.low = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.low:
            self.low.append(min(self.low[-1], val))
        else:
            self.low.append(val)

    def pop(self) -> None:
        temp = self.stack.pop(-1)
        self.low.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.low[-1]
