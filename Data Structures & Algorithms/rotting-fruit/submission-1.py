class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruitsCount = 0
        m = len(grid)
        n = len(grid[0])
        rottens = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshFruitsCount+=1
                elif grid[i][j] == 2:
                    rottens.append([i,j])
            
        count = 0
        while rottens and freshFruitsCount:
                size = len(rottens)
                for _ in range(size):
                    i,j = rottens.popleft()
                    for o_i,o_j in [[-1,0],[0,-1],[1,0],[0,1]]:
                        n_i, n_j = i+o_i, j+o_j
                        if n_i in range(m) and n_j in range(n) and grid[n_i][n_j] == 1:
                                freshFruitsCount -= 1
                                grid[n_i][n_j] = 2
                                rottens.append([n_i,n_j])
                count += 1

        return -1 if freshFruitsCount else count
        