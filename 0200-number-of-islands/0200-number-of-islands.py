class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        v = [[0] * m for _ in range(n)]
        
        def backtrack(i,j):
            if i<0 or j<0 or i>=n or j>=m:
                return
            if grid[i][j]=='0':
                return 
            if v[i][j]:
                return
            v[i][j]=1
            backtrack(i,j+1) 
            backtrack(i+1,j)
            backtrack(i,j-1)
            backtrack(i-1,j)
            
        r=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and not v[i][j]:
                    r+=1
                    backtrack(i,j)
        return r