class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def dfs(i,j):
            if i not in range(m) or j not in range(n):
                return 1
            if grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i,j))
            perimeter = 0
            perimeter += dfs(i+1, j)
            perimeter +=  dfs(i, j+1)
            perimeter += dfs(i-1, j)
            perimeter +=dfs(i, j-1)
            return perimeter

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return  dfs(i, j)
        return 0
    