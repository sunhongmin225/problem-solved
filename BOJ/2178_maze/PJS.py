# This was very similar to the tomato question

if __name__ == '__main__':
    row_col = input().split(' ')
    N = int(row_col[0])
    M = int(row_col[1])

    grid = []
    for i in range(N):
        single_row = input()
        grid.append([int(c) for c in single_row])
    
    visited = []
    for i in range(N):
        visited.append([0] * M)
    
    queue = [(0,0), (-1,-1)]
    visited[0][0] = 1
    cnt = 1

    while(len(queue) != 0):
        point = queue.pop(0)
        i = point[0]
        j = point[1]

        if i == N-1 and j == M-1:
            break

        if i == -1 and j == -1:
            cnt += 1
            if len(queue) != 0:
                queue.append((-1,-1))
            continue

        if (i-1 >= 0 and grid[i-1][j] == 1 and visited[i-1][j] == 0):
            queue.append((i-1, j))
            visited[i-1][j] = 1
        if (i+1 < N and grid[i+1][j] == 1 and visited[i+1][j] == 0):
            queue.append((i+1, j))
            visited[i+1][j] = 1
        if (j-1 >= 0 and grid[i][j-1] == 1 and visited[i][j-1] == 0):
            queue.append((i, j-1))
            visited[i][j-1] = 1
        if (j+1 < M and grid[i][j+1] == 1 and visited[i][j+1] == 0):
            queue.append((i, j+1))
            visited[i][j+1] = 1

    print(cnt)
