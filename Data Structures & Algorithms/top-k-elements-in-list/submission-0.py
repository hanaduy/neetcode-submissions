class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for key,value in count.items():
            heapq.heappush(result, (-value, key))

        output = []
        for i in range(k):
            c, num = heapq.heappop(result)
            output.append(num)
        return output