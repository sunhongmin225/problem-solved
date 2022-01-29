class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume_of_water = []
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height[i:]):
                h = min(h1, h2)
                volume_of_water.append(h * j)
        return max(volume_of_water)
