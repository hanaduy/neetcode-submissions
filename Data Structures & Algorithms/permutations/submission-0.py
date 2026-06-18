class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        visited = set()

        def dfs(cur):
            if len(path) == len(nums):
                result.append(path[:])

            for i in range(0, len(nums)):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    dfs(cur)
                    path.pop()
                    visited.remove(nums[i])
        
        dfs(0)

        return result