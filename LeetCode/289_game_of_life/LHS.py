class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]
        
        # count the number of live neighbors for each matrix component
        def count_lives(brd): 
            count = [[0 for i in range(n)] for j in range(m)]
            for y in range(m):
                for x in range(n):
                    cnt = 0
                    for src in range(8):
                        nx = x + dx[src]
                        ny = y + dy[src]
                        if nx >= 0 and nx < n and ny >= 0 and ny < m:
                            if brd[ny][nx] == 1:
                                cnt += 1
                    count[y][x] = cnt
            return count
        
        cnt = count_lives(board)
        # match conditions for live and dead cells respectively
        for y in range(m):
            for x in range(n):
                if board[y][x] == 1:
                    if cnt[y][x] < 2:
                        board[y][x] = 0
                    elif cnt[y][x] > 3:
                        board[y][x] = 0
                else:
                    if cnt[y][x] == 3:
                        board[y][x] = 1
