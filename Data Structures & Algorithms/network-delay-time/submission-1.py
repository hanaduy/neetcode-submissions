class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        heapq.heapify(heap)
        visited = {}

        heapq.heappush(heap, [0,k,0]) # Push start into the queue
        result = 0
        while heap:
            cur = heapq.heappop(heap)
            if cur[1] in visited:
                continue
            result = cur[0]
            visited[cur[1]] = cur[0]
            for time in times:
                target_node, weight = time[1],time[2]
                if time[0] == cur[1] and target_node not in visited:
                    heapq.heappush(heap, [cur[0]+weight,target_node])

        if len(visited) == n:
            return result
        return -1
