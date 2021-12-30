# TYPE: dynamic programming

MAX = 10000

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize the DP array
        dp = list() # [0, 1, 2, 3, ..., amount]   
        dp.append(0) # when amount equals 0
        
        # Sort the coins list
        coins.sort()
        
        for i in range(1, amount + 1):
            min_ = MAX
            for coin in coins:
                if i - coin >= 0:
                    # print(dp)
                    # print(f"amount:{amount} coin:{coin}")
                    if dp[i - coin] + 1 < min_:
                        min_ = dp[i - coin] + 1
                else:
                    break
            dp.append(min_)
            
        assert len(dp) == amount + 1
        
        return dp[amount] if dp[amount] < MAX else -1         