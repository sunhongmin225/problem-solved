# Lessons
# 1. DP 문제에서 i = 1, 2 일때의 값은 그냥 초기화를 하고 시작하는 게 낫겠다. 

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        s = 'd' + s # Note: 'd' is a dummy digit

        if s[1] == '0':
            return 0
        else:
            dp[0] = 1
            dp[1] = 1

        for i in range(2, len(s)):
            # NOTE: valid digits are from 1 to 26. 
            # Thus, Only need to check i-th digit and (i-1)th digit + i-th digit

            # 1. checking i-th digit
            new_group = int(s[i])
            if 1 <= new_group <= 9: 
                dp[i] += dp[i - 1]

            # 2. checking (i-1)th digit + i-th digit
            if s[i - 1] == '0' :
                continue
            else:
                new_group = int(s[i - 1] + s[i])
                if 10 <= new_group <= 26:
                    dp[i] += dp[i - 2]

        return dp[-1]


if __name__ == "__main__":
    # s = "12"
    # s = "226"
    # s = "06"
    s = "11106"
    print(Solution().numDecodings(s))