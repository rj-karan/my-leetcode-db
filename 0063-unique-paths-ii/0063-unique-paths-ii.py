class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp=[[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

    
        for j in range(m):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(n):
            for j in range(m):
                if not obstacleGrid[i][j]==1:
                    if not(i==0 or j==0):
                        dp[i][j]=dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j]=0
        print(dp)
        return dp[n-1][m-1]