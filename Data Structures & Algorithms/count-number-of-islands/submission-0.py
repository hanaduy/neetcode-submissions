class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        result = 0

        row, col = len(grid), len(grid[0])

        def dfs(i,j):
            if (i,j) in visited:
                return False
            if not (0<=i<row and 0<=j<col):
                return False
            if grid[i][j] == "0":
                return False
            visited.add((i,j))
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
            return True


        for i in range(0, row):
            for j in range(0, col):
                if dfs(i,j):
                    result += 1
        return result
