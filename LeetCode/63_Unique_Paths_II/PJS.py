class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    # if obstacle
                    continue
                if i == 0 and j == 0:
                    continue
                top = 0 if i-1 < 0 else dp[i-1][j]
                left = 0 if j-1 < 0 else dp[i][j-1]
                dp[i][j] = top + left
        
        return dp[-1][-1]
