class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        depth = len(word)
        print(m, n, depth)
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
    

        def find_word(i, j):
            visited = [[0 for x in range(n)] for y in range(m)]
            cnt = 1
            visited[i][j] = 1
            res = []
            res.append(word[0])
            fin = 0
            def dfs(i, j, cnt):
                print(f"dfs called {i} {j} {cnt}")
                for d in range(4):
                    ny = i + dy[d]
                    nx = j + dx[d]
                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        print(f"next {ny} {nx}")
                        
                        if visited[ny][nx] == 0:
                            if word[cnt] == board[ny][nx]:
                                visited[ny][nx] = 1
                                res.append(word[cnt])
                                print(res)
                                if cnt == depth-1:
                                    fin = 1
                                    return True
                                else:
                                    cnt += 1
                                    if dfs(ny, nx, cnt):
                                        return True
                                    else:
                                        return False

            return dfs(i, j, cnt)
        
        # do dfs only if the first char of word is the same as grid
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if depth == 1:
                        return True
                    print(f"word point: {i},{j}")
                    res = find_word(i, j)
                    if res == True:
                        return True
        return False

