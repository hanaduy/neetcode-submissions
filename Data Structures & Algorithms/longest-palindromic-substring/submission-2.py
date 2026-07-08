class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        length = []
        if len(s) == 1:
            return s

        for i in range(len(s)):
            if i == 0:
                length.append(1)
                result = s[0]
                prev = 1
            maxi = 1
            for j in range(i-1,max(i-prev-2,-1),-1):
                compare = s[j:i+1]
                if compare == compare[::-1]:
                    maxi = max(maxi,len(compare))
                    if len(compare)>=len(result):
                        result = compare    
            length.append(maxi)
            prev = maxi
        return result