class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        arth = ["+","-","*","/"]
        for i in tokens:
            if i in arth:
                num1 = stack.pop()
                num2 = stack.pop()
                print(num1, num2)
                stack.append(self.eval(int(num1),int(num2),i))
            else:
                stack.append(i)
        return int(stack[-1])

    def eval(self, num1, num2, expression):
        if expression == "+":
            return num1+num2
        if expression == "-":
            return num2-num1
        if expression == "*":
            return num1*num2
        if expression == "/":
            return num2/num1