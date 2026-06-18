class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = []
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = set()
        def dfs(x,y):
            if len(path) > len(word):
                return False
            
            if "".join(path) == word:
                return True

            for direction in directions:
                if len(board)>x+direction[0]>=0 and len(board[0])>y+direction[1]>=0 and (x+direction[0], y+direction[1]) not in visited:
                    path.append(board[x+direction[0]][y+direction[1]])
                    visited.add((x+direction[0], y+direction[1]))
                    if dfs(x+direction[0], y+direction[1]):
                        return True
                    path.pop()
                    visited.remove((x+direction[0], y+direction[1]))
                
            return False
        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    path.append(board[i][j])
                    visited.add((i,j))
                    if dfs(i,j):
                        return True
                    path.pop()
                    visited.remove((i,j))
        return False
