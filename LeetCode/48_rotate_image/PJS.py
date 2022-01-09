class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """       
        n = len(matrix)
        for i in range(n):
            matrix[i].reverse()
        
        # now we can take the symmetric version of 'matrix'
        for i in range(n):
            for j in range(n-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = tmp
