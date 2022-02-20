'''
1. First attempt: thought it's similar to n-queens, but I am still having hard time with DFS
2. Second attempt: referred to https://www.youtube.com/watch?v=pfiQ_PS1g8E 
'''

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # in order not to visit the same path

        def dfs(r, c, i):
            if i == len(word):
                return True

            # conditions to backtrack
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            # Found the character that I was looking for
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        # print(row, col)

        board_v = [[None] * col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                board_v[i][j] = [board[i][j], False]

        flag = False
        
        def dfs(index: int, i: int, j: int):
            if index == len(word) - 1:
                flag = True
                return # Found all alphabets in the word
            
            # 일단 visited 표시하고 & index + 1 하고 
            index += 1
            board_v[i][j][1] = True
            
            # 사방을 본다
            nx = [0, 0, 1, -1]
            ny = [1, -1, 0, 0]

            for k in range(4):
                if i + nx[k] < row and j + ny[k] < col: 
                    neighbor = board_v[i + nx[k]][j + ny[k]]
                    if neighbor[0] == word[index] and neighbor[1] == False:
                        dfs(index, i + nx[k], j + ny[k])
            
            index -= 1
            board_v[i][j][1] = False

        for i in range(row):
            for j in range(col):
                if board_v[i][j][0] == word[0]:
                    dfs(0, i, j)

        return flag
'''

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    print(Solution().exist(board, word))
