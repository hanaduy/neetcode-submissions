class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        total = 0
        path = []

        def dfs(start,total):
            if total == target:
                result.append(path[:])
                return
            if total> target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                total += nums[i]
                dfs(i, total)
                path.pop()
                total -= nums[i]
        dfs(0, 0)
        return result

            