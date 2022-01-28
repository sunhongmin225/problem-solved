# TYPE: BFS
# RETROSPECT
# 1. 정신을 차리자 (잔 실수가 너무 많았음ㅠ)

from typing import List
from collections import deque
import math


class Solution:
    def solve(self, N: int, M: int, arr: List[List[int]]) -> int:
        # tuple: (x, y, value, visited, shortest_path_from （0,0）)
        # 1. Reformat arr
        for i in range(N):
            for j in range(M):
                arr[i][j] = [i, j, arr[i][j], False, math.inf]

        # 2. Start BFS
        # 2-1. initialize
        neighbor_idx = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        queue = deque([])
        arr[0][0][3] = True
        arr[0][0][4] = 1
        queue.append(arr[0][0])

        while len(queue) != 0:
            # 큐에는 value 1인 것들만 들어온다고 가정
            curr = queue.popleft()
            
            # Visit neighbors
            for idx in neighbor_idx:
                
                x = curr[0] + idx[0]
                y = curr[1] + idx[1]
                if x >= 0 and x < N and y >= 0 and y < M: # boundary check
                    if arr[x][y][2] == 1 and arr[x][y][3] == False:
                        arr[x][y][3] = True
                        arr[x][y][4] = min(arr[x][y][4], curr[4] + 1)
                        
                        queue.append(arr[x][y])

        return arr[N-1][M-1][4]

        
if __name__ == "__main__":
    N, M = list(map(int, input().split(" ")))
    arr = []
    for _ in range(N):
        arr.append(list(map(int, list(input()))))

    assert len(arr) == N 
    assert len(arr[0]) == M       

    # N = 4
    # M = 6

    # # arr = [[1, 0, 1, 1, 1, 1],
    # #         [1, 0, 1, 0, 1, 0],
    # #         [1, 0, 1, 0, 1, 1],
    # #         [1, 1, 1, 0, 1, 1]]
    # arr = [[1, 1, 0, 1, 1, 0],
    #         [1, 1, 0, 1, 1, 0],
    #         [1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 0, 1]]


    ans = Solution().solve(N, M, arr)
    print(ans)
