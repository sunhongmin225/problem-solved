# Type: implementation

# Retrospect:
# 1. 예시 그림에서 행이나 열 별로 규칙이 보이길래 문제에서 주어진 recursion pattern을 무시하고 풀다가 풀이가 너무 복잡해짐. 
# 그래서 문제의 recursion pattern을 고려하면서 구현하려고 했더니 결과적으로 MID_IDX 하나만 둬도 깔끔하게 구현할 수 있었음.
# 문제 조건을 잘 활용하려고 해보자. 


class Solution:
    def solve(self, n: int, r: int, c: int) -> int:
        # initialize
        GROUP = None
        MID_IDX = int((2 ** n) / 2)
        ans = 0

        while MID_IDX >= 1:
            if r >= MID_IDX and c >= MID_IDX:
                GROUP = 3
            elif r >= MID_IDX and c < MID_IDX:
                GROUP = 2
            elif r < MID_IDX and c >= MID_IDX:
                GROUP = 1
            elif r < MID_IDX and c < MID_IDX:
                GROUP = 0

            ans += GROUP * (MID_IDX ** 2)

            # index 재조정
            r = r - MID_IDX if r >= MID_IDX else r # NOTE: 주의. 여기 logic 다시 읽어보기
            c = c - MID_IDX if c >= MID_IDX else c
            MID_IDX = int(MID_IDX / 2)
        
        return ans

if __name__ == "__main__":
    n, r, c = list(map(int, input().split(" ")))

    print(Solution().solve(n, r, c))

