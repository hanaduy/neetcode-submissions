class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        result = []

        for i in range(0, len(nums)):
            if i-2<0:
                result.append(nums[i])
            else:
                previous = 0 if i-3 < 0 else result[i-3]
                result.append(nums[i]+max(result[i-2],previous))
        
        return max(result[-1],result[-2])