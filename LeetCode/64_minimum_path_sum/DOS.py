from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp
        m, n = len(grid), len(grid[0])
        
        # init
        tbl = [[0 for _ in range(n)] for _ in range(m)]
        tbl[-1][-1] = grid[-1][-1]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if i+1 <= m-1 and j+1 <=n-1:
                    tbl[i][j] = grid[i][j] + min(tbl[i+1][j], tbl[i][j+1])
                elif i+1 > m-1:
                    tbl[i][j] = grid[i][j] + tbl[i][j+1]
                elif j+1 > n-1:
                    tbl[i][j] = grid[i][j] + tbl[i+1][j]
                    
        return tbl[0][0]