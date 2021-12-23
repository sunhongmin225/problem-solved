class Solution:
    def coinChange(self, coins, amount: int) -> int:
        def get_shortest_combo(coins, amount, mem=None):
            if mem is None:
                mem = {}
            if amount in mem:
                return mem[amount]
            if amount == 0:
                return []
            if amount < 0:
                return -1
            shortest_combo = -1
            for c in coins:
                remainder = amount - c
                remainder_combo = get_shortest_combo(coins, remainder, mem)
                if remainder_combo != -1:
                    combo = [*remainder_combo, c]
                    if shortest_combo == -1 or len(combo) < len(shortest_combo):
                        shortest_combo = combo
            mem[amount] = shortest_combo
            return mem[amount]
        result = get_shortest_combo(coins, amount)
        return len(result) if result != -1 else -1



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