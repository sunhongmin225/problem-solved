from itertools import product
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = dy = [1, 0, -1]
        dxdy = list(product(dx,dy))
        nrow, ncol = len(board), len(board[0])
        next_states = make_states(nrow, ncol)
            
        def get_next_state(i,j):
            n_neighbors = 0
            now_state = board[i][j]
            for di, dj in dxdy:
                if di == dj == 0:
                    continue
                ni = i+di
                nj = j+dj
                if 0<=ni<nrow and 0<=nj<ncol:
                    if board[ni][nj] == 1:
                        n_neighbors += 1
                        
            if now_state == 0:
                if n_neighbors == 3:
                    return 1
                return 0
            elif now_state == 1:
                if n_neighbors < 2:
                    return 0
                elif n_neighbors < 4:
                    return 1
                return 0
            
        for i in range(nrow):
            for j in range(ncol):
                next_states[(i,j)] = get_next_state(i,j)
        
        for (i,j), v in next_states.items():
            board[i][j] = v
            

def make_states(nrow, ncol) -> dict:
    d = {}
    for t in product(range(nrow), range(ncol)):
        d[t] = 0
    return d
