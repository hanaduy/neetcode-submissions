class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums
        prefix = [nums[0]]
        suffix = deque([nums[-1]])
        

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])
        
        for i in range(len(nums)-2, -1, -1):
            suffix.appendleft(suffix[0] * nums[i])

        result = [suffix[1]]
        for i in range(1, len(nums)-1):
            result.append(prefix[i-1]*suffix[i+1])
        return result+[prefix[-2]]