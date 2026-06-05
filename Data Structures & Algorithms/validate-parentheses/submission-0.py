class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        print(stack)
        for c in s:
            if len(stack)>0 and self.inPair(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
        print(stack)
        return len(stack) == 0

    def inPair(self, a,b):
        if (a == "(" and b ==")") or (a == "[" and b =="]") or ( a == "{" and b =="}"):
            return True
        return False

