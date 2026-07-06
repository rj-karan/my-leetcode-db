class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx=0
        sy=0
        dx=0
        dy=0
        od=0
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    sx=i
                    sy=j
                if grid[i][j]==2:
                    dx=i
                    dy=j
                if grid[i][j]==-1:
                    od+=1
                c+=1
        oc=c-od
        r=0
        sol=[[0]*len(grid[0]) for i in range(len(grid))]
        def backtrack(i,j,grid,sol,step):
            nonlocal r
            if i<0 or j<0 or j>=len(grid[0]) or i>=len(grid) or grid[i][j]==-1 or sol[i][j]==1:
                return False
            if grid[i][j]==2:
                if step==oc:
                    r+=1
                return False
            sol[i][j]=1
            if backtrack(i,j+1,grid,sol,step+1):
                return True
            if backtrack(i+1,j,grid,sol,step+1):
                return True
            if backtrack(i,j-1,grid,sol,step+1):
                return True
            if backtrack(i-1,j,grid,sol,step+1):
                return True
            sol[i][j]=0
            return False
        backtrack(sx,sy,grid,sol,1)
        return r