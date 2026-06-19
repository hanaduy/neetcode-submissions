class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        result = []
        path = []

        def dfs(cur):
            if len(path) == len(digits):
                result.append("".join(path[:]))
                return

            char = mapping[digits[cur]]
            for i in range(0,len(char)):
                path.append(char[i])
                dfs(cur+1)
                path.pop()
            return
        
        if not digits:
            return []
        dfs(0)
        return result
            
