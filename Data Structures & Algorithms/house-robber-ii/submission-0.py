class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_sub(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            
            result = [0]*len(nums)
            result[0], result[1] = nums[0], max(nums[0],nums[1])

            for i in range(2, len(nums)):
                result[i] = max(result[i-2]+nums[i], result[i-1])
            
            return result[-1]

        return max(rob_sub(nums[1:]), rob_sub(nums[:-1]))