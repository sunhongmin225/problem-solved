from collections import deque

def get_bj_input():
    nrow, ncol = map(int, input().split())
    matrix = []
    for _ in range(nrow):
        row = [int(d) for d in str(input())]
        matrix.append(row)
    return nrow, ncol, matrix

    
class Maze:

    def __init__(self, nrow, ncol, maze) -> None:
        self.maze = maze
        self.row_range = range(nrow)
        self.col_range = range(ncol)
        self.start = (0,0)
        self.end = (nrow-1, ncol-1)

    def bfs(self):
        visited = set()
        q = deque()
        paths = {}
        q.appendleft(self.start)
        while q:
            i, j = q.pop()
            if (i,j) == self.end:
                break
            visited.add((i,j))
            if i-1 in self.row_range and self.maze[i-1][j] == 1 and (i-1,j) not in visited:
                # up
                q.appendleft((i-1,j))
                paths[(i-1,j)] = (i,j)
            if j-1 in self.col_range and self.maze[i][j-1] == 1 and (i,j-1) not in visited:
                # left
                q.appendleft((i,j-1))
                paths[(i,j-1)] = (i,j)
            if i+1 in self.row_range and self.maze[i+1][j] == 1 and (i+1,j) not in visited:
                # down
                q.appendleft((i+1,j))
                paths[(i+1,j)] = (i,j)
            if j+1 in self.col_range and self.maze[i][j+1] == 1 and (i,j+1) not in visited:
                # right
                q.appendleft((i,j+1))
                paths[(i,j+1)] = (i,j)
        return paths
    
    def get_shortest_path(self):
        paths = self.bfs()
        position = self.end
        result = [position]
        while position != self.start:
            position = paths[position]
            result.append(position)
        return result

    def get_shortest_path_length(self):
        length = 1
        paths = self.bfs()
        position = self.end
        while position != self.start:
            position = paths[position]
            length += 1
        return length

    def solve(self):
        result = self.get_shortest_path_length()
        return result

# 제출용 코드
print(Maze(*get_bj_input()).solve())



if __name__=="__main__":
    nrow, ncol = 4, 6
    mat = []
    in1 = "101111"
    in2 = "101010"
    in3 = "101011"
    in4 = "111011"
    mat.append([int(d) for d in in1])
    mat.append([int(d) for d in in2])
    mat.append([int(d) for d in in3])
    mat.append([int(d) for d in in4])
    print(Maze(nrow, ncol, mat).solve())

    nrow, ncol = 4, 6
    mat = []
    in1 = "110110"
    in2 = "110110"
    in3 = "111111"
    in4 = "111101"
    mat.append([int(d) for d in in1])
    mat.append([int(d) for d in in2])
    mat.append([int(d) for d in in3])
    mat.append([int(d) for d in in4])
    print(Maze(nrow, ncol, mat).solve())

    nrow, ncol = 2, 25
    mat = []
    in1 = "1011101110111011101110111"
    in2 = "1110111011101110111011101"
    mat.append([int(d) for d in in1])
    mat.append([int(d) for d in in2])
    print(Maze(nrow, ncol, mat).solve())

    nrow, ncol = 7, 7
    mat = []
    in1 = "1011111"
    in2 = "1110001"
    in3 = "1000001"
    in4 = "1000001"
    in5 = "1000001"
    in6 = "1000001"
    in7 = "1111111"
    mat.append([int(d) for d in in1])
    mat.append([int(d) for d in in2])
    mat.append([int(d) for d in in3])
    mat.append([int(d) for d in in4])
    mat.append([int(d) for d in in5])
    mat.append([int(d) for d in in6])
    mat.append([int(d) for d in in7])
    print(Maze(nrow, ncol, mat).solve())