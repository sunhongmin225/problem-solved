from typing import List


## Ref https://velog.io/@haebin/Leetcode-221.-Maximal-Square
def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end='')
        print()
    print()

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        square = [[0 for i in range(col+1)] for j in range(row+1)]
        #print_matrix(square)
        max_width = 0
        for y in range(row):
            for x in range(col):
                if matrix[y][x] == "1":
                    square[y+1][x+1] = min(square[y][x], square[y+1][x], square[y][x+1]) + 1
                    if max_width < square[y+1][x+1]:
                        max_width = square[y+1][x+1]

        #print_matrix(square)
        return max_width**2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#matrix = [["0","1"],["0","1"]]
#matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
print("Matrix")
print_matrix(matrix)
Solution().maximalSquare(matrix)
