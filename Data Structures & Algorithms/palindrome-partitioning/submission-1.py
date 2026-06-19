class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def dfs(start):
            if start == len(s):
                result.append(path[:])
                return

            for i in range(start+1, len(s)+1):
                if s[start:i] == s[start:i][::-1]:
                    path.append(s[start:i])
                    dfs(i)
                    path.pop()
        dfs(0)
        return result
