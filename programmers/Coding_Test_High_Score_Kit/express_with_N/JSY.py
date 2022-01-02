# -*- coding: utf-8 -*-
# type: DP
# First attempt: 
# 최소 개수의 N == 최소 개수의 N으로 표현할 수 있는 최대값은? 
# 근데 위는 추측이고, 이래야만 하는 이유는 잘 모르겠음. 
# Second attempt:
# 2차 DP로 풀어야 함. 열은 num of min, 행은 연산 타입별로. 
# 그럼 연산의 좌우 중 어디로 넣음? 
# Third attempt:
# 외부 reference 참고

# Retrospect
# 1. DP 문제가 배열 형태로만 풀릴 거라고 생각하지 말자
# 2. How to use set: python set expects iterable as an input
# 3. Python itertools.product
# 4. edge case! 

import itertools

def solution(N, number):
    if number == N:
        answer = 1
    else: 
        answer = -1
        # 1. create a list to store groups for 8 numbers and initialize the list
        dp_arr = [None] * 9
        dp_arr[1] = set([N])
        
        for i in range(2, 9):
            temp = set([int(str(N)*i)])  # without calculation

            for j in range(1, i):
                # calculate between group_j and group_(i - j)
                temp2 = []

                for x, y in list(itertools.product(dp_arr[j], dp_arr[i - j])):
                    temp2.append(x + y)
                    temp2.append(x - y)
                    temp2.append(x * y)
                    if y != 0:
                        temp2.append(x / y)
        
                temp.update(temp2)

            dp_arr[i] = temp

            # check if there is number in i's group
            if number in dp_arr[i]:
                answer = i
                break

    return answer


if __name__ == "__main__":
    N = 2
    number = 11
    answer = solution(N, number)
    print(answer)
    