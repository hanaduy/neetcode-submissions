class MinStack:

    def __init__(self):
        self.mini = float("inf")
        self.stack = deque()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.mini = val
        else:
            self.stack.append(val-self.mini)
            self.mini = min(val, self.mini)

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp < 0:
            self.mini = self.mini - temp
            

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.mini
        else:
            return self.stack[-1] + self.mini

    def getMin(self) -> int:
        return self.mini
        
