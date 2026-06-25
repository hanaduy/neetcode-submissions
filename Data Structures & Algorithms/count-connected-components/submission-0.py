class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [x for x in range(n)]
        result = 0

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            x = find(x)
            y = find(y)

            if x!=y:
                parent[y] = x
                return True
            
            return False
        
        for edge in edges:
            union(edge[0], edge[1])

        for i in range(len(parent)):
            if i == parent[i]:
                result += 1
        
        return result 


