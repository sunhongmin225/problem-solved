class Solution:
    grid = None
    m = None
    n = None
    answer = None
    def numIslands(self, grid) -> int:
        """
        Loop rows & columns of grid and increment number of island
        """
        if self.grid is None:
            self.grid = grid
        if self.m is None:
            self.m = len(self.grid)
        if self.n is None:
            self.n = len(self.grid[0])
        if self.answer is None:
            self.answer = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == '1':
                    self.visit_island(i, j)
                    self.answer += 1
        return self.answer

    def visit_island(self, i, j):
        """
        recursive island visiting method
        """
        if not (0<=i<self.m and 0<=j<self.n) or self.grid[i][j] != "1":
            return
        self.grid[i][j] = 'v'
        self.visit_island(i+1, j)
        self.visit_island(i, j+1)
        self.visit_island(i-1, j)
        self.visit_island(i, j-1)


if __name__=="__main__":
    grid = [  
  ["1","1","1","1","0"],  
  ["1","1","0","1","0"],  
  ["1","1","0","0","0"],  
  ["0","0","1","0","1"]  
]
    s = Solution()
    print(s.numIslands(grid))