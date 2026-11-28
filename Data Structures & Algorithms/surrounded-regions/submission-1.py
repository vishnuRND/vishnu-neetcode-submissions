class Solution:
    def solve(self, board: List[List[str]]) -> None:

        boundaries = set()
        m = len(board)
        n = len(board[0])
        queue = deque()
        visited = set()
        for i in range(m):
            if board[i][0] == "O":
                queue.append([i,0])
            if board[i][n-1] == "O":
                queue.append([i,n-1])

        for j in range(n):
            if board[0][j] == "O":
                queue.append([0,j])
            if board[m-1][j] == "O":
                queue.append([m-1,j])

        while queue:
            i, j = queue.popleft()
            visited.add((i,j))
            for di, dj in [[-1,0],[0,-1],[1,0],[0,1]]:
                ni,nj = i+di, j+dj
                if ni in range(m) and nj in range(n) and board[ni][nj] == "O" and (ni, nj) not in visited:
                    queue.append([ni, nj])

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"


    
        