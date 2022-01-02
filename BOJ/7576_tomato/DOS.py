from collections import deque

def get_bj_input():
    m, n = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    return n, m, grid


class Solution:
    def __init__(self, n, m, grid) -> None:
        self.n = n
        self.m = m
        self.grid = grid
        self.ripe_tomatoes = self.get_ripe_tomatoes()
        self.expected_tomatoes = self.get_expected_tomatoes()
        self.time = 0

    def solve(self):
        while self.ripe_tomatoes:
            if self.expected_tomatoes == len(self.get_ripe_tomatoes()):
                return self.time
            self.time+=1
            for _ in range(len(self.ripe_tomatoes)):
                i, j = self.ripe_tomatoes.popleft()
                neighbors = [(i+1, j), (i-1, j), (i,j+1), (i,j-1)]
                for _i, _j in neighbors:
                    if 0<=_i<self.n and 0<=_j<self.m and self.grid[_i][_j] == 0:
                        self.ripe_tomatoes.append((_i, _j))
                        self.grid[_i][_j] = 1
        return -1

    def get_ripe_tomatoes(self):
        result = deque()
        for i in range(n):
            for j in range(m):
                if self.grid[i][j] == 1:
                    result.append((i,j))
        return result

    def get_expected_tomatoes(self):
        result = self.n * self.m
        for i in range(n):
            for j in range(m):
                if self.grid[i][j] == -1:
                    result -= 1
        return result


if __name__=="__main__":
    # m, n = 6, 4
    # matrix = [
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 1],
    # ]
    # print(Solution(n, m, matrix).solve()) # 8

    # m, n = 6, 4
    # matrix = [
    #     [0,-1,0,0,0,0],
    #     [-1,0,0,0,0,0],
    #     [0,0,0,0,0,0],
    #     [0,0,0,0,0,1],
    # ]
    # print(Solution(n, m, matrix).solve()) # -1 

    n, m, matrix = get_bj_input()
    s = Solution(n, m, matrix).solve()
    print(s)