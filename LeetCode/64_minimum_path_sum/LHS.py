class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for y in range(m):
            for x in range(n):
                # grid[0][0] initial point
                if x == 0 and y == 0:
                    continue
                # grid[y][0] left-most column
                elif x == 0 and y != 0:
                    dp[y][x] = grid[y][x] + dp[y-1][x]
                # grid[0][x] top row
                elif x != 0 and y == 0:
                    dp[y][x] = grid[y][x] + dp[y][x-1]
                # remains
                else:
                    dp[y][x] = grid[y][x] + min(dp[y-1][x], dp[y][x-1])
        return(dp[-1][-1])

