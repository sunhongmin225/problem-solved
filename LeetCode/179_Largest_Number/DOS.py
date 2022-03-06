"""
1. tried to implement while loop and pop nums
2. failed

ref: https://leetcode.com/problems/largest-number/discuss/1727431/Python-solution
"""
from typing import List
from collections import defaultdict


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = ''

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = str(nums[i]) + str(nums[j])
                b = str(nums[j]) + str(nums[i])
                if a < b:
                    nums[i], nums[j] = nums[j], nums[i]

        for num in map(str, nums):
            ans += num
        return str(int(ans))

