import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        last_result = None
        while l <= r:
            mid = (l+r)//2
            time_taken = sum([math.ceil(x/mid) for x in piles])
            print(mid, time_taken)

            if time_taken < h:
                r = mid - 1
                last_result = mid
            elif time_taken > h:
                l = mid + 1
            else:
                r = mid - 1
                last_result = mid
        return last_result
        
            
            
