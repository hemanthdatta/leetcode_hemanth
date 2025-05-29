class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        maxarea=0
        def bfs(r,c):
            a=1
            q=collections.deque()
            grid[r][c]=0
            q.append((r,c))
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if (nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]==0):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc]=0
                    a=a+1
            return a


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area=bfs(r,c)
                    maxarea=max(area,maxarea)
        return maxarea


        