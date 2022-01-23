import math

def solution(N, r, c):
    if N == 1:
        # when 2 x 2 square, return the trivial count.
        return 2 * r + c

    # largest sq is the length of the largest subsquare of the grid
    largest_sq = math.pow(2, N-1)

    # r_ind and c_ind is the r, c row indices
    # looking at 'largest_sq x largest_sq' square as a whole
    r_ind = r // largest_sq
    c_ind = c // largest_sq

    # new_r and new_c are the r and c indices within a subsquare
    new_r = r - r_ind * largest_sq
    new_c = c - c_ind * largest_sq

    # all counts in the previous subsquares (the one that doesn't contain our coordinate of interest) 
    # + recursively calling the count within the subsquare
    cnt = largest_sq**2 * (r_ind * 2 + c_ind) + solution(N-1, new_r, new_c)
    return cnt


if __name__ == '__main__':
    var = input().split(' ')
    N = int(var[0])
    r = int(var[1])
    c = int(var[2])

    print(int(solution(N, r, c)))
