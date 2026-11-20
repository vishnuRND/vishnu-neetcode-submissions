class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = dict()
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            if i not in range(m) or j not in range(n):
                return 
            if grid[i][j] == "0":
                return 
            if (i, j) in visited:
                return 
            visited[(i, j)] = True
            for d_i, d_j in [[-1,0],[0,-1],[1,0],[0,1]]:
                n_i, n_j = i+d_i, j+d_j
                dfs(n_i, n_j)


        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count+=1

        return count
        