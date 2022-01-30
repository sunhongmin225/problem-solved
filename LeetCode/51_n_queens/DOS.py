from typing import List

class Solution:
    board = None
    solutions = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = []
        for _ in range(n):
            self.board.append([0] * n)
        self.main(n, 0)
        solution = [["." if rune == 0 else "Q" for rune in row] for row in self.board]
        return solution
            
    def main(self, n, nqueen):
        if n == nqueen:
            return True
        for i in range(n):
            for j in range(n):
                if self.is_queen_valid(i,j,n):
                    self.board[i][j] = 1
                    nqueen += 1
                    if self.main(n, nqueen) == True:
                        return True
                    self.board[i][j] = 0
                    nqueen -= 1
        return False
    
    def is_queen_valid(self, row, col, n):
        if not self.queen_in_col(row, col, n) and \
            not self.queen_in_row(row, col, n) and \
            not self.queen_in_left_down_diag(row, col, n) and \
            not self.queen_in_left_up_diag(row, col, n) and \
            not self.queen_in_right_down_diag(row, col, n) and \
            not self.queen_in_right_up_diag(row, col, n):
            return True
        return False

    def queen_in_row(self, row, col, n):
        for i in range(n):
            if self.board[row][i] == 1:
                return True
        return False

    def queen_in_col(self, row, col, n):
        for i in range(n):
            if self.board[i][col] == 1:
                return True
        return False

    def queen_in_left_down_diag(self, row, col, n):
        while row in range(n) and col in range(n):
            if self.board[row][col] == 1:
                return True
            row += 1
            col -= 1
        return False

    def queen_in_left_up_diag(self, row, col, n):
        while row in range(n) and col in range(n):
            if self.board[row][col] == 1:
                return True
            row -= 1
            col += 1
        return False

    def queen_in_right_down_diag(self, row, col, n):
        while row in range(n) and col in range(n):
            if self.board[row][col] == 1:
                return True
            row += 1
            col += 1
        return False

    def queen_in_right_up_diag(self, row, col, n):
        while row in range(n) and col in range(n):
            if self.board[row][col] == 1:
                return True
            row -= 1
            col -= 1
        return False

if __name__=="__main__":
    print(Solution().solveNQueens(4))
    print(Solution().solveNQueens(1))
