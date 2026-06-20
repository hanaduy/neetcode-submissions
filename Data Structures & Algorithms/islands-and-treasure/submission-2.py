class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i,j,0))

        while queue:
            i,j,level = queue.popleft()
            grid[i][j] = min(grid[i][j], level)
            for direct in direction:
                if not(0<=i+direct[0]<row and 0<=j+direct[1]<col):
                    continue
                if level < grid[i+direct[0]][j+direct[1]]:
                    queue.append((i+direct[0],j+direct[1],level+1))

        return


