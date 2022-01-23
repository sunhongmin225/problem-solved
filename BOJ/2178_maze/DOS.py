def get_bj_input():
    nrow, ncol = map(int, input().split())
    matrix = []
    for _ in range(nrow):
        row = [int(d) for d in str(input())]
        matrix.append(row)
    return nrow, ncol, matrix

    


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
    print(mat)