class Solution:
    def is_finished(self, grid, visited):
        """
        Returns position of unvisited land if such position exits, 
        else returns (-1, -1)
        """
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if (int(item) == 1 and not visited[i][j]):
                    return (i, j)
        return (-1,-1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = []
        m = len(grid)
        n = len(grid[0])
        
        visited = []
        for _ in range(m):
            visited.append([False]*n)
        
        start_point = self.is_finished(grid, visited)
        num_islands = 0
        
        while(start_point != (-1,-1)):
            # if in this loop, it means there is a new island that is not explored yet.
            queue = [start_point]
            
            while(len(queue) != 0):
                # this searches for all positions of the land that are connected to the start_point
                point = queue.pop(0)
                i = point[0]
                j = point[1]
                
                visited[i][j] = True
                
                if (i-1 >= 0 and int(grid[i-1][j]) == 1 and not visited[i-1][j]):
                    queue.append((i-1, j))
                if (i+1 < m and int(grid[i+1][j]) == 1 and not visited[i+1][j]):
                    queue.append((i+1, j))
                if (j-1 >= 0 and int(grid[i][j-1]) == 1 and not visited[i][j-1]):
                    queue.append((i, j-1))
                if (j+1 < n and int(grid[i][j+1]) == 1 and not visited[i][j+1]):
                    queue.append((i, j+1))
            
            # out of the while loop if no more neighboring positions are found.
            num_islands += 1
            start_point = self.is_finished(grid, visited)
            
        return num_islands
