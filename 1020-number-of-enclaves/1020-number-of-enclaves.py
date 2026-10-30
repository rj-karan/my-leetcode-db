from collections import deque

class Solution:
    def numEnclaves(self,grid:list[list[int]])->int:
        n=len(grid)
        m=len(grid[0])
        q=deque()

        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or i==n-1 or j==m-1) and grid[i][j]==1:
                    q.append((i,j))
                    grid[i][j]=0

        d=[(0,1),(1,0),(0,-1),(-1,0)]

        while q:
            r,c=q.popleft()

            for dr,dc in d:
                nr=r+dr
                nc=c+dc

                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1:
                    grid[nr][nc]=0
                    q.append((nr,nc))

        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    count+=1

        return count