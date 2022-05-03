class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [collections.defaultdict(int) for _ in range(len(nums) + 1)] # a list of dictionaries
        # holds key = possible sum upto the ith number
        #       value = the count of ways that add upto that sum
        
        dp[0][0] = 1
        
        # for each ith number, check the ith possible sum / cnt 
        # and update the i+1th place
        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i + 1][sum + num] += cnt
                dp[i + 1][sum - num] += cnt
        return dp[len(nums)][target]
