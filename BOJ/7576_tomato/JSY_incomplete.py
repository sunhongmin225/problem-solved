# Type: BFS

from collections import deque
import itertools
import math

INF = math.inf

def solution():
    M, N = map(int, input().split())
    
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # Overview: 
    # For each tomato, update the least day that it will get ripen.
    # Get the max of the mins.
    ripen = [[INF]*M]*N
    # print(ripen)
    answer = -INF
    # TODO: should print 0 if all tomatoes are ripen from start

    # for i, j in list(itertools.product(range(N), range(M))):
    for i in range(N):
        for j in range(M):
            start = arr[i][j] # mistake: arr[i, j]

            if start == 1:
                # Try BFS
                # 1. Initialize
                day = 0
                queue = deque([])
                queue.append((i, j))

                while len(queue) != 0:
                    x, y = queue.popleft()
                    # print(f"x, y: {x, y}")
                    day += 1

                    # Boundary check!! 
                    if x - 1 >= 0:
                        if arr[x - 1][y] == 0:
                            queue.append((x - 1, y))
                            arr[x - 1][y] = 1 # switch to ripen
                            if ripen[x - 1][y] > day:
                                ripen[x - 1][y] = day
                                if day > answer:
                                    answer = day

                    if x + 1 < N:
                        # print(x + 1, y)
                        if arr[x + 1][y] == 0:
                            queue.append((x + 1, y))
                            arr[x + 1][y] = 1
                            if ripen[x + 1][y] > day:
                                ripen[x - 1][y] = day
                                if day > answer:
                                    answer = day
                    if y - 1 >= 0:
                        if arr[x][y - 1] == 0:
                            queue.append((x, y - 1))
                            arr[x][y - 1] = 1
                            if ripen[x][y - 1] > day:
                                ripen[x][y - 1] = day
                                if day > answer:
                                    answer = day
                    if y + 1 < M:
                        if arr[x][y + 1] == 0:
                            queue.append((x, y + 1))
                            arr[x][y + 1] = 1
                            if ripen[x][y + 1] > day:
                                ripen[x][y + 1] = day
                                if day > answer:
                                    # print(day)
                                    answer = day

            
    # check for the all already ripen
    if answer == -INF:
        answer = 0

    # checking for left upriped fruits
    for i, j in list(itertools.product(range(N), range(M))):
        if arr[i][j] == 0:
            answer = -1
            break
    
    print(answer)

if __name__ == "__main__":
    solution()
   
