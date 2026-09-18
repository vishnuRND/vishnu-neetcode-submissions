class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)
        row = len(board[0])
        col = len(board)

        for i in range(row):
            for j in range(col):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxs[(i//3,j//3)]:
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxs[(i//3,j//3)].add(board[i][j])
        return True


        