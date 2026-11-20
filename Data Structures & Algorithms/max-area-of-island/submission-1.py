class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        result = 0
        def dfs(i, j):
            if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j] == 0:
                return 0
            count = 1
            grid[i][j] = 0
            for di, dj in [[-1,0],[0,-1],[1,0],[0,1]]:
                ni, nj = i+di, j+dj 
                count += dfs(ni, nj)
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))
        
        return result
        