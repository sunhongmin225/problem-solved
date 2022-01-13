# Retrospect
# 1. ^와 **는 다르다. ^는 exclusive-or이다. 
# 2. 문제를 잘 읽자. reversing x에 대해서도 boundary condition을 확인했어야 했다. 


class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        orig = x

        if -2**31 <= x <= 2**31 - 1:
            # take the minus sign off
            x = str(x)[1:] if x < 0 else str(x)
            # reverse -> int
            x = int(x[::-1])
            # put the minus sign on
            x = x * -1 if orig < 0 else x
            # Check boundary condition
            ans = x if -2**31 <= x <= 2**31 - 1 else 0 

        return ans


if __name__ == "__main__":
    solution = Solution()
    INT = 1534236469
    print(solution.reverse(INT))