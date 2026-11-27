class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        def dfs(index, i, j):
            if index == len(word):
                return True
            if not (i in range(len(board)) and j in range(len(board[0]))) or board[i][j] != word[index] :
                return False
            tmp = board[i][j]
            board[i][j] = "#"
            for di, dj in [[-1,0],[0,-1],[1,0],[0,1]]:
                    ni,nj = i+di, j+dj
                    res = dfs(index+1, ni, nj)
                    if res:
                        board[i][j] = tmp
                        return True

            board[i][j] = tmp
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    word_found = dfs(0, i,j)
                    if word_found:
                        return True
        
        return False
        