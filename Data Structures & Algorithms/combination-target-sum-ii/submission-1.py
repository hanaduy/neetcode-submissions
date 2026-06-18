class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        total = 0
        path = []
        candidates.sort(key=lambda x: x)

        def dfs(cur, total):
            # print(path)
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(cur, len(candidates)):
                if i>cur and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, total+candidates[i])
                path.pop()
            
            return

        dfs(0, 0)
        return result