class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort(key=lambda x:x)

        def dfs(cur):
            result.append(path[:])

            for i in range(cur, len(nums)):
                if i>cur and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i+1)
                path.pop()

        dfs(0)
        return result