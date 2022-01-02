class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        island = 0
        visit = [[0 for i in range(n)] for j in range(m)]
        # print(visit)
        
        def dfs(i, j):
            if(i<0 or i>=m or j<0 or j>=n or grid[i][j]=="0"):
                return
            if(visit[i][j] == 1):
                return
            else:
                visit[i][j] = 1
            dfs(i-1, j) 
            dfs(i, j-1) 
            dfs(i+1, j) 
            dfs(i, j+1)
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == "1" and visit[i][j] == 0):
                    # print("i: " + str(i))
                    # print("j: " + str(j))
                    island += 1
                    dfs(i, j)
        print(visit)
        return island