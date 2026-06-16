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
            if heap:
                cur = heapq.heappop_max(heap)
                count, task = cur[0], cur[1]
                result.append(task)
                if count-1 > 0:
                    queue[task] = (n+1,count-1)
            else:
                result.append("idle")

            expired = []
            for k,v in queue.items():
                left = v[0]-1
                count = v[1]
                if left == 0:
                    heapq.heappush_max(heap,(count,k))
                    expired.append(k)
                else:
                    queue[k] = (left, count)
            for k in expired:
                del queue[k]
        return len(result)



                