class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        result = deque()
        for i in range(len(temperatures)-1, -1, -1):
            if not stack:
                stack.appendleft(i)
                result.appendleft(0)
            else:
                while stack and temperatures[i] >= temperatures[stack[0]]:
                    stack.popleft()
                result.appendleft(stack[0]-i if stack else 0)
                stack.appendleft(i)
        return list(result)


            


            