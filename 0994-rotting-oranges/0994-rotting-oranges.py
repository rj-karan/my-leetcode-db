class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q=deque()
        f=0
        
        row=len(grid)
        col=len(grid[0])
        
        for r in range(row):
            for j in range(col):
                if grid[r][j]==2:
                    q.append([r,j])
                elif grid[r][j]==1:
                    f+=1

        m=0
        while q and f>0:
            for i in range(len(q)):
                r,c=q.popleft()
                d=[(0,1),(1,0),(0,-1),(-1,0)]
                for dr,dc in d:
                    nr=dr+r
                    nc=dc+c
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        f-=1
                        q.append([nr,nc])
            m+=1
        if f==0:
            return m
        else:
            return -1