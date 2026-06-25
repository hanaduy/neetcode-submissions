class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [x for x in range(0,len(edges)+1)]

        def find(x):
            if parent[x] != x:
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
            if not union(edge[0],edge[1]):
                return edge
        
        return None

