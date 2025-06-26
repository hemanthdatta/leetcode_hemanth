class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        q=deque([(0,0,1)])

        visit=set((0,0))
        di=[[0,1],[1,0],[-1,-1],[1,1],[-1,0],[0,-1],[-1,1],[1,-1]]
        while q:
            r,c,l=q.popleft()
            if (min(r,c)<0 or max(r,c)>=n or grid[r][c]):
                continue
            if r==n-1 and c==n-1:
                return l
            for dr,dc in di:
                if (r+dr,c+dc) not in visit:
                    q.append((r+dr,c+dc,l+1))
                    visit.add((r+dr,c+dc))
        return -1





                    

        