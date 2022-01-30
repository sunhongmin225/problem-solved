from collections import deque

shape = input().split()
N = int(shape[0])
M = int(shape[1])

rows = []
for i in range(N):
  rows.append(input())

## visited check
visit = [[0 for i in range(M)] for j in range(N)]
## distance from (0,0)
dist = [[1 for i in range(M)] for j in range(N)]

## next direction: right/up/left/down
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
visit[0][0] = 1
q.append((0,0))
while q:
  now = q.popleft()
  x = now[1]
  y = now[0]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (nx >= 0) and (nx < M) and (ny >= 0) and (ny < N):
      if (rows[ny][nx] == '1') and (visit[ny][nx] == 0):
        dist[ny][nx] = dist[y][x] + 1
        visit[ny][nx] = 1
        q.append((ny, nx))

print(dist[N-1][M-1])
