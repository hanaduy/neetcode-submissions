class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    queue.append((i,j,0))
                if grid[i][j] == 1:
                    grid[i][j] = 100
        result = 0
        while queue:
            i,j,level = queue.popleft()
            grid[i][j] = min(grid[i][j],level)
            result = max(grid[i][j],result)
            for direction in directions:
                if not (0<=i+direction[0]<row and 0<=j+direction[1]<col):
                    continue
                if grid[i+direction[0]][j+direction[1]] == 0:
                    continue
                if level+1<grid[i+direction[0]][j+direction[1]]:
                    queue.append((i+direction[0],j+direction[1],level+1))
        print(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 100:
                    return -1
        return result 