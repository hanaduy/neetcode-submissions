class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(i,j,visited):
            if not (0<=i<row and 0<=j<col):
                return False
            if board[i][j] == "X":
                return True
            # When i,j is valid and is "O", it is a little tricky. That means it is neighbour of another "O"
            # If it is already visited, we do not need to care about the previous level's status, just return 
            # True, saying it is enclosed.

            # For the outsider, if it has "X" neighbor and "O" neighbor, then itself is enclosed until one neighbor
            # is not enclosed.
            if (i,j) in visited:
                return True
            
            is_surrouded = True
            visited.add((i,j))
            for direction in directions:
                nxt = dfs(i+direction[0], j+direction[1],visited)
                is_surrouded = is_surrouded and nxt
            return is_surrouded

        for i in range(0,row):
            for j in range(0,col):
                
                if board[i][j]=="O":
                    visited = set()
                    if dfs(i,j,visited):
                        print(visited)
                        for visit in visited:
                            board[visit[0]][visit[1]] = "X"
                
        