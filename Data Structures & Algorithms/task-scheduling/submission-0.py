class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = OrderedDict()
        counter = defaultdict(int)
        for k,v in enumerate(tasks):
            counter[v] += 1
        
        heap = []
        heapq.heapify_max(heap)
        for k,v in counter.items():
            heapq.heappush_max(heap,(v,k)) # Count, Task
        
        result = []
        while heap or queue:
            expired = []
            for k,v in queue.items():
                queue[k] = [v[0]-1,v[1]]
                if v[0]-1 == 0:
                    heapq.heappush_max(heap,(v[1],k))
                    expired.append(k)
            for k in expired:
                del queue[k]

            if heap:
                cur = heapq.heappop_max(heap)
                count, task = cur[0], cur[1]
                result.append(task)
                if count-1 > 0:
                    queue[task] = (n+1,count-1)
            else:
                result.append("idle")

        print(result)
        return len(result)



                