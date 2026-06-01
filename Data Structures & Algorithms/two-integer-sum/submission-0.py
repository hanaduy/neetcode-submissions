class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}

        for i in range(0,len(nums)):
            if nums[i] in need:
                return [need[nums[i]], i]
            else:
                need[target-nums[i]] = i