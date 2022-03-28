from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        if ROW == COL == 1:
            return grid[0][0]
        
        else:   
            # initialize dp array
            dp = [[0] * COL for i in range(ROW)]
            dp[0][0] = grid[0][0]

            # fill dp array
            for i in range(ROW):
                for j in range(COL):
                    if i == 0:
                        # if it is the first row, no path coming from top
                        dp[i][j] = dp[i][j - 1] + grid[i][j]
                    elif j == 0:
                        # if it is the first COL, no path coming from left
                        dp[i][j] = dp[i - 1][j] + grid[i][j]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

            return dp[ROW - 1][COL - 1]
        