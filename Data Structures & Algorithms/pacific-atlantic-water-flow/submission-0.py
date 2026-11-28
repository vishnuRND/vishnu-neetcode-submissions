class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()


        def recur(i, j,visit, prevHeight):
            if (i,j) in visit or (i not in range(m) or j not in range(n)) or heights[i][j] < prevHeight:
                return
            visit.add((i,j))
            for di, dj in [[-1,0],[0,-1],[1,0],[0,1]]:
                ni, nj = i+di, j+dj
                recur(ni,nj, visit, heights[i][j])


        for i in range(n):
            recur(0, i, pacific, heights[0][i])
            recur(m-1, i, atlantic, heights[m-1][i])

        for i in range(m):
            recur(i, 0, pacific, heights[i][0])
            recur(i, n-1, atlantic, heights[i][n-1])

        result = list()
        for i in range(m):
                for j in range(n):
                    if (i,j) in pacific and (i,j) in atlantic:
                        result.append([i,j])

        return result



        

        

      