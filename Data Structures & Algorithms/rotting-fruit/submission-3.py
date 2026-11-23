class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
            queue = deque()
            time = 0
            freshoranges = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        queue.append([i,j])
                    elif grid[i][j] == 1:
                        freshoranges+=1
            if freshoranges == 0:
                return 0
            time = 0
            while queue:
                len_q = len(queue)
                for _ in range(len_q):
                    q_i, q_j = queue.popleft()
                    for d_i, d_j in [[-1,0],[0,-1],[0,1],[1,0]]:
                        n_i, n_j = q_i+d_i, q_j+d_j
                        if n_i in range(len(grid)) and n_j in range(len(grid[0])) and grid[n_i][n_j] == 1:
                                freshoranges-=1
                                grid[n_i][n_j] = 2
                                queue.append([n_i,n_j])
                time+=1
            return time - 1 if freshoranges == 0 else -1
        