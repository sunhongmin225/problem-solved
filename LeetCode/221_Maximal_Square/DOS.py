from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nrows, ncols = len(matrix), len(matrix[0])
        max_side = 0
        tbl = [] # init dp table
        for _ in range(nrows+1):
            row = []
            for _ in range(ncols+1):
                row.append(0)
            tbl.append(row)

        # (i,j) bottom-right
        for i in range(1, nrows+1):
            for j in range(1, ncols+1):
                top_right = tbl[i-1][j]
                top_left = tbl[i-1][j-1]
                bot_left = tbl[i][j-1]
                if matrix[i-1][j-1] == '0':
                    continue
                tbl[i][j] = min(top_right, top_left, bot_left) + 1
                max_side = max(max_side, tbl[i][j])

        return max_side ** 2

