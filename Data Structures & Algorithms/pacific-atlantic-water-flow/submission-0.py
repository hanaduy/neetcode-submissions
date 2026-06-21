class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(i,j,visited):
            if (i,j) in visited:
                return

            visited.add((i,j))
            for direction in directions:
                if not (0<=i+direction[0]<row and 0<=j+direction[1]<col):
                    continue
                if heights[i][j] <= heights[i+direction[0]][j+direction[1]]:
                    dfs(i+direction[0], j+direction[1], visited)
                

        for i in range(row):
            dfs(i,0,pac) # Starting Pacific
            dfs(i,col-1,atl) # Starting Atlantic

        for i in range(col):
            dfs(0,i,pac) # Starting Pacific
            dfs(row-1,i,atl) # Starting Atlantic

        res = []
        for r in range(row):
            for c in range(col):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
        