class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        diff = set()

        for i in nums:
            if i not in diff:
                diff.add(i)
            else:
                return True

        return False
        