class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_sum = [0] * 10002
        num_min, num_max = 10002, 0
        # sum up the same numbers,
        # num_min/max found for efficient looping later
        for num in nums :
            num_sum[num] += num
            num_min = min(num, num_min)
            num_max = max(num, num_max)
        
        
        dp = [0] * 10002
        dp[num_min] = num_sum[num_min]
        for index in range(num_min+1, num_max+1) :
            # either take the index-1 th number or
            # take the index-2 th number and then taks the current number
            dp[index] = max(dp[index-1], dp[index-2]+num_sum[index])

        return dp[num_max]
        
        return take;
