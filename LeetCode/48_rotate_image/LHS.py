class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ans = []
        
        ## read matrix reverse column-wise
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(matrix[n-j-1][i])
            ans.append(tmp)

        for i in range(n):
            matrix[i] = ans[i]