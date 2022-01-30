"""
1. 너무 처음부터 최적화를 생각하지는 않아도 될 거 같다. 한 칸씩만 옮기는 것도 괜찮다. 어차피 O(N)이다. 
"""
from typing import List

INF = -1

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx = 0
        right_idx = len(height) - 1
        max_area = INF
        
        while (right_idx - left_idx > 0):
            width = right_idx - left_idx
            min_height_idx = left_idx if height[left_idx] < height[right_idx] else right_idx
            max_area = max(max_area, height[min_height_idx] * width)
            if min_height_idx == left_idx: 
                left_idx += 1
            else:
                right_idx -= 1

        return max_area

if __name__ == "__main__":
    # height = [1,1]
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))