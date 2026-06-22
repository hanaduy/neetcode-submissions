class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = [0,0]

        for i in range(2, len(cost)+1):
            cur_min = min(result[i-2]+cost[i-2], result[i-1]+cost[i-1])
            result.append(cur_min)
        
        return result[-1]