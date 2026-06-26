class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        heap = []
        heapq.heappush(heap, [0,0])
        total = 0

        while len(visited) < len(points):
            cur = heapq.heappop(heap)
            cost,idx = cur[0], cur[1]
            x1,y1 = points[idx][0], points[idx][1]
            
            if idx in visited:
                continue
            visited.add(idx)
            total += cost

            for i in range(len(points)):
                if i not in visited:
                    x2,y2 = points[i][0], points[i][1]
                    cur_dist = abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(heap,[cur_dist,i])
        return total

