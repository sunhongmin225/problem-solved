class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            res[i-1] = prices[i] - prices[i-1]
            if res[i-1] < 0:
                res[i-1] = max(res[i-1], 0)
        return(sum(res))
