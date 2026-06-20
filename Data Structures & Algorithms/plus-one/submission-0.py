class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        result = []
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                cur = digits[i]+carry+1
            else:
                cur = digits[i]+carry

            if cur >= 10:
                carry = 1
                cur = cur % 10
            else:
                carry = 0
            result.append(cur)

        if carry == 1:
            result.append(1)
        
        return result[::-1]