class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(cur, s):
            if len(s) == 0:
                result.append(cur)
                return
            
            for i in range(1,len(s)+1):
                if s[:i] == s[:i][::-1]:
                    dfs(cur+[s[:i]], s[i:])
        
        dfs([], s)

        return result
