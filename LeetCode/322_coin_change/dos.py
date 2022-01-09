class Solution:
    def coinChange(self, coins, amount: int) -> int:
        """
        via tabulation
        """
        tbl = [None] * (amount+1)
        tbl[0] = []
        for i, v in enumerate(tbl):
            if v is not None:
                for c in coins:
                    if (i+c) < (amount+1):
                        combo = [*tbl[i], c]
                        if tbl[i+c] is None or len(tbl[i+c]) > len(combo):
                            tbl[i+c] = combo
        result = tbl[amount]
        return len(result) if result is not None else -1


if __name__ == '__main__':
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(s.coinChange(coins, amount))

    s = Solution()
    coins = [2]
    amount = 3
    print(s.coinChange(coins, amount))

    s = Solution()
    coins = [1]
    amount = 0
    print(s.coinChange(coins, amount))

    s = Solution()
    coins = [186, 419, 83, 408]
    amount = 6249
    print(s.coinChange(coins, amount))