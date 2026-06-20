class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        row, col = len(grid), len(grid[0])
        visited = set()

        def dfs(i,j):
            if not (0<=i<row and 0<=j<col):
                return 0
            
            if (i,j) in visited:
                return 0
            
            if grid[i][j] == 0:
                return 0

            visited.add((i,j))
            return sum([dfs(i+1,j),dfs(i-1,j),dfs(i,j-1),dfs(i,j+1)])+1


        for i in range(0, row):
            for j in range(0, col):
                result = max(result, dfs(i,j))
        
        return result

