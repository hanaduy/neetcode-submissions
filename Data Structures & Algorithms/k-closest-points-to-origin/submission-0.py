class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for point in points:
            x,y = point[0], point[1]
            distance = (x**2 + y**2)**1/2
            heapq.heappush(heap,(distance,x,y))

        result = []
        for i in range(k):
            temp = heapq.heappop(heap)
            result.append([temp[1], temp[2]])
        return result
        