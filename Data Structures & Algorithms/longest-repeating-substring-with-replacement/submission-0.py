class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = defaultdict(int)
        l = 0
        result = 0
        maxi = 0
        for r in range(0, len(s)):
            charSet[s[r]] += 1
            maxi = max(maxi, charSet[s[r]])

            while (r-l+1)-maxi > k:
                charSet[s[l]] -= 1
                l += 1

            result = max(result, r-l+1)

        return result
            
