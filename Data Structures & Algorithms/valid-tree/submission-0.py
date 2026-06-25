class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        track = [x for x in range(n)]
        total = []

        def find(x):
            while track[x] != x:
                x = track[x]    
            return x
        
        def union(x,y):
            x = find(x)
            y = find(y)

            if x != y:
                track[y] = x
                total.append(1)
                return True
            return False
            
        for pair in edges:
            if not union(pair[0], pair[1]):
                return False
        
        if sum(total) != n-1:
            return False
        return True