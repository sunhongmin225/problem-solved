from math import comb
from typing import List
import itertools 

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # 1. Get combinations of two nums (i.e. nC2)
        combinations = [list(x) for x in itertools.combinations(nums, 2)]

        # 2. Make a dictionary with <key: the product of two nums, value: the two nums>
        products = {}
        for item in combinations:
            product = item[0] * item[1]
            if product in products:
                products[product].append(item)
            else:
                products[product] = [item]
        
        ans = 0
        for k, v in products.items():
            if len(v) >= 2:
                # nCr where n = len(v), c = 2
                num_combinations = comb(len(v), 2) 
                ans += num_combinations * 8

        return ans

if __name__ == "__main__":
    # nums =  [2,3,4,6]
    nums = [1, 2, 3, 4, 6, 12]
    # nums = [1, 2, 4, 5, 10]

    print(Solution().tupleSameProduct(nums))