class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        completed = 0
        result = []
        while queue:
            cur = queue.popleft()
            result.append(cur)
            completed +=1
            for neighbor in adj_list[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if completed !=numCourses:
            return []
        return result