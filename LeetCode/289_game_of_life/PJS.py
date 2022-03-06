import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        tmp = copy.deepcopy(board)
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                alive = (tmp[i][j] == 1)
                
                def get_live_neigh(i_, j_):
                    cnt = 0
                    for i_idx in range(max(0, i_-1), min(m, i_+2)):
                        for j_idx in range(max(0, j_-1), min(n, j_+2)):
                            if tmp[i_idx][j_idx] == 1:
                                cnt += 1
                    return cnt
                
                num_live_neigh = get_live_neigh(i, j)
                if alive:
                    num_live_neigh -= 1
                  
                if alive and (num_live_neigh < 2 or num_live_neigh > 3):
                    board[i][j] = 0
                
                if not alive and num_live_neigh == 3:
                    board[i][j] = 1
