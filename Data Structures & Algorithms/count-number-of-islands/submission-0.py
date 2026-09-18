class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visited = set()
        def dfs(i, j):
            if i == m or j == n:
                return 
            visited.add((i,j))
            for o_i, o_j in [[-1,0],[0,-1],[1,0],[0,1]]:
                n_i, n_j = i+o_i, j+o_j
                if n_i in range(m) and n_j in range(n) and grid[n_i][n_j] == "1" and (n_i,n_j) not in visited:
                    dfs(n_i, n_j)
        
        count = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count += 1
        
        return count
        