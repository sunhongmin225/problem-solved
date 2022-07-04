class Solution:
## solution referred to https://leetcode.com/problems/unique-paths-ii/discuss/2018995/C%2B%2B-oror-Easy-to-Understand-oror-DP-Top-Down
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ly = len(obstacleGrid)
        lx = len(obstacleGrid[0])
        dp = [[0 for i in range(lx)] for j in range(ly)]
        for i in range(ly):
            if obstacleGrid[i][0] == 1:
                break;
            dp[i][0] = 1
        for i in range(lx):
            if obstacleGrid[0][i] == 1:
                break;
            dp[0][i] = 1
        for i in range(1, ly):
            for j in range(1, lx):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


## Time out
#    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#        if(obstacleGrid[0][0]==1):
#            return 0
#        self.cnt = 0
#        self.obstacleGrid = obstacleGrid
#        self.ly = len(obstacleGrid)
#        self.lx = len(obstacleGrid[0])
#        self.pathFinding(0, 0)
#        # print(self.cnt)
#        return self.cnt
#    def pathFinding(self, y, x):
#        if y == self.ly-1 and x == self.lx-1:
#            self.cnt += 1
#            return
#        if y+1 < self.ly and self.obstacleGrid[y+1][x]!=1:
#            self.pathFinding(y+1, x)
#        if x+1 < self.lx and self.obstacleGrid[y][x+1]!=1:
#            self.pathFinding(y, x+1)
        
