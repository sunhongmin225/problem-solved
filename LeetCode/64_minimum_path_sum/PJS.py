# Using dp to solve
import sys

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                else:
                    top_value = dp[i-1][j] if i > 0 else float('inf')
                    bottom_value = dp[i][j-1] if j > 0 else float('inf')
                    dp[i][j] = min(top_value, bottom_value) + grid[i][j]
                    
        return dp[m-1][n-1]
