class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if(obstacleGrid[0][0]==1):
            return 0
        self.cnt = 0
        self.obstacleGrid = obstacleGrid
        self.ly = len(obstacleGrid)
        self.lx = len(obstacleGrid[0])
        self.pathFinding(0, 0)
        # print(self.cnt)
        return self.cnt
    def pathFinding(self, y, x):
        if y == self.ly-1 and x == self.lx-1:
            self.cnt += 1
            return
        if y+1 < self.ly and self.obstacleGrid[y+1][x]!=1:
            self.pathFinding(y+1, x)
        if x+1 < self.lx and self.obstacleGrid[y][x+1]!=1:
            self.pathFinding(y, x+1)
        
