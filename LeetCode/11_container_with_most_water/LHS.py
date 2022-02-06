class Solution:
    def maxArea(self, height: List[int]) -> int:
        num = len(height)
        water = 0
        for i in range(num-1):
            for j in range(i+1, num):
                if j == i+1:
                    picked_index = j
                    picked_height = height[j]
                else:
                    if height[j] >= picked_height:
                        picked_index = j
                        picked_height = height[j]
                    else:
                        prev_max = min(height[i], picked_height) * (picked_index-i)
                        curr_max = min(height[i], height[j]) * (j-i)
                        if curr_max >= prev_max:
                            picked_index = j
                            picked_height = height[j]

                water = max(water, (picked_index-i)*min(height[i], picked_height))
                #water = max(water, min(height[i], height[j]) * (j - i))
        #print(water)
        return water
