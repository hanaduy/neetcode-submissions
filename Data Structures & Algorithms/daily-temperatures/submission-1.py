class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for k, v in enumerate(temperatures):
            while stack and temperatures[k] > temperatures[stack[-1]]:
                idx = stack.pop(-1)
                result[idx] = k-idx
            
            stack.append(k)
        return result

            


            


            