class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_check = [[False] * 10 for _ in range(9)]
        cols_check = [[False] * 10 for _ in range(9)]
        box_check  = [[False] * 10 for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                number = board[i][j]
                if number!=".":
                    number = int(number)
                    box_index = (3* (i//3)) + j//3
                    if rows_check[i][number] or cols_check[j][number] or box_check[box_index][number]:
                        return False
                    rows_check[i][number] = True
                    cols_check[j][number] = True
                    box_check[box_index][number] = True
        
        return True