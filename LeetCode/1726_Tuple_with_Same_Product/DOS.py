from itertools import combinations
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        ans = 0
        d = defaultdict(set)
        nums = sorted(nums)

        for i in range(len(nums)):
            for j in range(i):
                left, right = nums[j], nums[i]
                mul = left * right
                d[mul].add((left, right))

        for mul, pairs in d.items():
            if len(pairs) > 1:
                num_combinations = sum(1 for _ in combinations(pairs,2))
                ans += num_combinations * 2 * 2 * 2
        return ans

