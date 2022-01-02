#TYPE: BFS

# Retrospect
# 1. edge case !
# 2. boundary check!! 

import collections
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for each element in grid, perform BFS
        m = len(grid)
        n = len(grid[0])
        total = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid = self.markVisited(i, j, grid) # reassign grid
                    total += 1
        return total
        
        
    def markVisited(self, i: int, j: int, grid: List[List[str]]) -> List[List[str]]:
        # always found an island
        # return grid and mark already visited elements as '-1'

        m = len(grid)
        n = len(grid[0])
        
        deq = deque([])
        
        # add start point to queue and mark it as visited
        deq.append((i, j))
        grid[i][j] = '-1'
        
        while deq:
            x, y = deq.popleft() 
            
            # Check for 4 neighbor elements
            # Put all unvisited neighborhood nodes into queue and mark them visited
            if x - 1 >= 0: # boundary check for left node
                if grid[x - 1][y] == '1':
                    deq.append((x - 1, y))
                    grid[x - 1][y] = '-1'
            if x + 1 < m: # boundary check for right node
                if grid[x + 1][y] == '1':  
                    deq.append((x + 1, y))
                    grid[x + 1][y] = '-1'
            if y - 1 >= 0: # boundary check for the node above
                if grid[x][y - 1] == '1': 
                    deq.append((x, y - 1))
                    grid[x][y - 1] = '-1'
            if y + 1 < n: # boundary check for the node below
                if grid[x][y + 1] == '1':
                    deq.append((x, y + 1))
                    grid[x][y + 1] = '-1'
        
        return grid
        

if __name__ == '__main__':
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
    ]

    solution = Solution()
    num_of_islands = solution.numIslands(grid)
    print(num_of_islands)
