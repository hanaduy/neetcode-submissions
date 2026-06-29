class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0,0
        result = 0
        current_set = set()

        while l<=r and r < len(s):
            if s[r] not in current_set:
                current_set.add(s[r])
                result = max(result, r-l+1)
                r += 1
            else:
                current_set.remove(s[l])
                l+=1
        return result