# I brought this because I heard that this problem is a CSP (Constraint Satisfaction Problem)
# so I thought I could solve it but understanding the theoretical stuff and actually implementing it are so much different...
# Referenced: https://velog.io/@woo1031/Leetcode-51.-N-Queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.count = 0
        visited = [0] * n 
        answers = []
    
        def dfs(row):
            def is_ok_on(nth_row):
                # for a given nth_row, check if it has conflicts with other rows
                for rows in range(nth_row): 
                    if visited[nth_row] == visited[rows] or\
                        nth_row - rows == abs(visited[nth_row] - visited[rows]):
                        # if there is a conflict, return False
                        return False  
                return True
            
            if row >= n:
                # when we've come to the last row without failing
                self.count += 1
                grid = [['.'] * n for _ in range(n)]
                for idx, value in enumerate(visited):
                    # visited list holds in which columns the queens will be placed for a certain row
                    grid[idx][value] = 'Q'
                result = []
                for row in grid:
                    result.append(''.join(row))
                answers.append(result)
                return 
    
            for col in range(n):
                visited[row] = col
                if is_ok_on(row):
                    dfs(row + 1)                
        
        dfs(0)
        return answers
        
        
        
    """
    def is_violation(self, coor1, coor2):
        # returns true if violation of contraint
        if coor1[0] == coor2[0]:
            # in same row
            return True
        if coor1[1] == coor2[1]:
            # in same column
            return True
        if abs(coor1[0] - coor1[1]) == abs(coor2[0] - coor2[1]):
            # diagonally connected
            return True
        return False
    """
