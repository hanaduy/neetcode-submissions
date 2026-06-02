class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        block = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in row[i]:
                    row[i].add(board[i][j])
                else:
                    return False
                if board[i][j] not in col[j]:
                    col[j].add(board[i][j])
                else:
                    return False
                block_idx = (i//3, j//3)
                if board[i][j] not in block[block_idx]:
                    block[block_idx].add(board[i][j])
                else:
                    return False
        # print(row, col, block)

        return True