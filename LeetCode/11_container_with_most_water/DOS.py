from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # time limit exceeded O(n^2)
        max_volume = 0
        for i, h_i in enumerate(height):
            for j, h_j in enumerate(height[:i]):
                volume = (i-j) * min(h_i, h_j)
                max_volume = max(max_volume, volume)
        return max_volume


if __name__=="__main__":
    height = [1,8,6,2,5,4,8,3,7]
    output = 49
    print(Solution().maxArea(height))

    height = [1,1]
    output = 1
    print(Solution().maxArea(height))
