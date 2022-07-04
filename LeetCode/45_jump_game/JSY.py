from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        MAX = 2000
        # intialize
        n = len(nums)
        dp = [0] * n

        for i in range(1, n):
            dp[i] = MAX
            for j in range(i):
                if i <= nums[j] + j and dp[j] != MAX: 
                    dp[i] = min(dp[i], dp[j] + 1)
                    break

        return dp[n - 1]


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(Solution().jump(nums))