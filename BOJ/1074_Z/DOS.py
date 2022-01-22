def get_bj_input():
    n, r, c = map(int, input().split())
    return n, r, c


def get_sum_list(n, r, c):
    sum_list = []
    if n == 1:
        if r == c == 0:
            sum_list.append(0)
        elif r == 0 and c == 1:
            sum_list.append(1)
        elif r == 1 and c == 0:
            sum_list.append(2)
        elif r == c == 1:
            sum_list.append(3)
    else:
        nrow = ncol = 2 ** n
        previous_r = r-nrow/2
        previous_c = c-ncol/2
        previous_quad_len = 2**(n-1) * 2**(n-1)
        if previous_r >= 0 and previous_c >= 0:
            sum_list.append(3*previous_quad_len)
            sum_list.extend(get_sum_list(n-1, previous_r, previous_c))
        elif previous_r >= 0:
            sum_list.append(2*previous_quad_len)
            sum_list.extend(get_sum_list(n-1, previous_r, c))
        elif previous_c >= 0:
            sum_list.append(previous_quad_len)
            sum_list.extend(get_sum_list(n-1, r, previous_c))
        else:
            sum_list.extend(get_sum_list(n-1, r, c))
    return sum_list


def main():
    """
    백준 제출용 main 함수

    제출시 코드 최종라인에 print(main())
    """
    return sum(get_sum_list(*get_bj_input()))


if __name__=="__main__":
    print(sum(get_sum_list(3, 1, 1)))
