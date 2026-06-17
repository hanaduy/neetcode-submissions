class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        queue = deque([[x] for x in range(len(nums))])
        while queue:
            cur = queue.popleft()
            cur_nums = [nums[x] for x in cur]
            result.append(cur_nums)
            for i in range(cur[-1]+1, len(nums)):
                temp = cur[:]
                temp.append(i)
                queue.append(temp)
               
        result.append([])
        return result