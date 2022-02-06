"""
1. First attempt: Totally misunderstood the rule of chess
2. Second attempt: got an aid from this link (https://www.youtube.com/watch?v=Ph95IHmRp5M)
3. This was my first time solving backtracking. Should have more practice on these types of Qs.
""" 

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        res = []
        board = [["."] * n for i in range(n)] # will reuse this for every row
        
        
        def backtrack(r):
            if r == n: # stop condition
                copy = ["".join(r) for r in board]
                res.append(copy)
                return

            # should specify column 
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue # should skip to the next column

                # We have found the right position to place the queen.
                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                # should unplace the queen from the board. 
                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res


#     def solveNQueens(self, n: int) -> List[List[str]]:
#         # seat available: 1 / taken: 0 / unavailable because of attack: -1
#         grid = [[1] * n] * n
#         print(grid)

#         for i in range(n):
#             for j in range(n):
#                 self.find_seat(i, j, grid, num_queens)

#     def find_seat(self, i: int, j: int, grid: List[List[str]], num_queens: int):
#         grid[i][j] = 0
#         num_queens -= 1

#         dx = [1, 0, -1]
#         dy = [1, 0, -1]

#         for x in dx:
#             for y in dy:
#                 if 0 =< x + dx < n and 0 =< y + dy < n:
#                     grid[x + dx][y + dy] = -1
        
#         for m in range(len(grid)):
#             for n in range(len(grid)):
#                 if grid[m][n] == 1:
#                     find_seat(m, n, grid, num_queens)
        
#         return grid



# if __name__ == "__main__":
#     print(Solution().solveNQueens(3))