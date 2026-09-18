class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        treasures = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    treasures.append([i,j,0])

        while treasures:
            i,j, distance = treasures.popleft()
            if grid[i][j] < distance:
                continue  
            grid[i][j] = distance
            for o_i, o_j in [[-1,0],[0,-1],[1,0],[0,1]]:
                n_i, n_j = i+o_i, j+o_j
                if n_i in range(m) and n_j in range(n) and grid[n_i][n_j]!=-1:
                            treasures.append([n_i,n_j, distance+1])
            