class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            heapq.heappush_max(stones, abs(stone1-stone2))
        
        return stones[0] if len(stones) == 1 else 0
