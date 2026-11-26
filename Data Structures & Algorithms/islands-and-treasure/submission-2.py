class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
            queue = deque()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                            queue.append([i,j,0])
            
            while queue:
                len_queue = len(queue)
                for _ in range(len_queue):
                        x, y,dist = queue.popleft()
                        for di, dj in [[-1,0],[0,-1],[1,0],[0,1]]:
                            ni, nj = x+di, y+dj
                            if ni in range(len(grid)) and nj in range(len(grid[0])) and grid[ni][nj] > dist+1:
                                grid[ni][nj] = dist+1
                                queue.append([ni, nj, dist+1])

                                
        
        

        