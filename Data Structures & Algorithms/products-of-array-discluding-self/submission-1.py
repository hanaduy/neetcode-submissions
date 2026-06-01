class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = 1
        cnt = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                prod *= nums[i]
        if cnt >= 2:
            return [0]*len(nums)
        
        for i in range(0, len(nums)):
            if cnt == 0:
                result.append(prod//nums[i])
            else:
                result.append(0) if nums[i] != 0 else result.append(prod)

        return result