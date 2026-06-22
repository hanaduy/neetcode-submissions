class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {}
        adj_list = defaultdict(list)
        for i in range(0,numCourses):
            indegree[i] = 0
        
        for prerequisite in prerequisites:
            indegree[prerequisite[0]] += 1
            adj_list[prerequisite[1]].append(prerequisite[0])
        
        queue=deque()
        for k,v in indegree.items():
            if v == 0:
                queue.append(k)

        while queue:
            cur = queue.popleft()
            for neighbor in adj_list[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        result = True
        for k,v in indegree.items():
            if v>0:
                result = False
        return result