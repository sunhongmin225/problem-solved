'''
- still not used to backtracking.
'''
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow = len(board)
        ncol = len(board[0])
        up, down, left, right = (0,1), (0,-1), (-1,0), (1,0)
    
        def backtrack(i,j,runes):
            # basecase
            if not runes:
                return True
            if i < 0 or i == nrow or j < 0 or j == ncol or board[i][j] != runes[0]:
                return False

            # recursion
            result = False
            board[i][j] = '!' # visiting i,j
            for dx, dy in [up, down, left, right]:
                result = backtrack(i+dx, j+dy, runes[1:])
                if result:
                    break
            board[i][j] = runes[0] # complete visit; restore value
            return result
            
        for i in range(nrow):
            for j in range(ncol):
                if backtrack(i,j,word):
                    return True
        return False
            