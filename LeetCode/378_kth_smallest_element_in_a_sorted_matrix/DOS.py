"""[summary]
was not familiar with bisection search or heap data structure
https://www.youtube.com/watch?v=0d6WF79hQME
"""
from typing import List
from bisect import bisect_right

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]
        
        def get_smaller_val_idx(val):
            idx = 0
            for i in range(n):
                idx += bisect_right(matrix[i], val)
            return idx
        
        while left < right:
            mid = (left+right)//2
            if get_smaller_val_idx(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
                
            