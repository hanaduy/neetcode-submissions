import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r)//2
            time_taken = sum([math.ceil(x/mid) for x in piles])

            if time_taken <= h:
                r = mid - 1
            elif time_taken > h:
                l = mid + 1

        return l
        
            
            
