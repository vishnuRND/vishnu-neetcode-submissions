class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(i, j):
            visited.add((i,j))
            count = 1
            for o_i, o_j in [[0,-1],[-1,0],[0,1],[1,0]]:
                n_i, n_j = i+o_i, j+o_j
                if n_i in range(m) and n_j in range(n) and (n_i,n_j) not in visited and grid[n_i][n_j] == 1:
                        count += dfs(n_i, n_j)
            return count

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    result = max(result, dfs(i,j))
            
        return result
                    

            
            