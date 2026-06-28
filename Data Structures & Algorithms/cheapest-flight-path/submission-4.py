class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        heap = []
        adj_list = defaultdict(list)
        visited = {}
        weight = defaultdict()
        for flight in flights:
            adj_list[flight[0]].append(flight[1])
            weight[(flight[0],flight[1])] = flight[2]
        # print(weight,adj_list)
        heapq.heappush(heap, [0,src,0])
        while heap:
            dist, node, level = heapq.heappop(heap)
            if level > k+1:
                continue
            if node == dst:
                return dist
            if (node, level) in visited and visited[(node, level)] <= dist:
                continue
            
            visited[(node, level)] = dist
            for neighbor in adj_list[node]:
                heapq.heappush(heap, [dist+weight[(node,neighbor)],neighbor,level+1])
            
        return -1 if dst not in visited else visited[dst]