class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        final = 0

        for i in range(0, len(nums)):
            num_set.add(nums[i])

        for i in range(0, len(nums)):
            result = 0
            if nums[i] -1 not in num_set:
                current = nums[i]
                while current in num_set:
                    result += 1
                    current += 1
            if result >= final:
                final = result
        
        return final