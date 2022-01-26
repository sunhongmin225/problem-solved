import sys
from pathlib import Path
sys.path.append(Path(__file__).parent.parent.resolve().__str__())
from boj_testing import Case, TestSet

from collections import deque


def get_bj_input():
    nrow, ncol = map(int, input().split())
    matrix = []
    for _ in range(nrow):
        row = [int(d) for d in str(input())]
        matrix.append(row)
    return nrow, ncol, matrix

def main(meta, inputs):
    nrow, ncol = [int(d) for d in meta]
    maze = [[int(d) for d in row] for row in inputs]
    row_range = range(nrow)
    col_range = range(ncol)
    start = (0, 0)
    end = (nrow-1, ncol-1)
    q = deque()
    q.appendleft(start)
    while q:
        i, j = q.pop()
        if (i,j) == end:
            break
        if i-1 in row_range and maze[i-1][j] == 1:
            # up
            q.appendleft((i-1,j))
            maze[i-1][j] = maze[i][j] + 1
        if j-1 in col_range and maze[i][j-1] == 1:
            # left
            q.appendleft((i,j-1))
            maze[i][j-1] = maze[i][j] + 1
        if i+1 in row_range and maze[i+1][j] == 1:
            # down
            q.appendleft((i+1,j))
            maze[i+1][j] = maze[i][j] + 1
        if j+1 in col_range and maze[i][j+1] == 1:
            # right
            q.appendleft((i,j+1))
            maze[i][j+1] = maze[i][j] + 1
    return maze[end[0]][end[1]]

   
# 제출용 코드
# nrow, ncol, matrix = get_bj_input()
# meta = [nrow, ncol]
# inputs = matrix
# print(main(meta, inputs))

if __name__=="__main__":
    t = TestSet()

    raw = '''
    4 6
    101111
    101010
    101011
    111011
    '''
    Case(raw, 15).add_to_test(t)

    raw = '''
    2 25
    1011101110111011101110111
    1110111011101110111011101
    '''
    Case(raw, 38).add_to_test(t)

    raw = """
    7 7
    1011111
    1110001
    1000001
    1000001
    1000001
    1000001
    1111111
    """
    Case(raw, 13).add_to_test(t)

    t.run(main)