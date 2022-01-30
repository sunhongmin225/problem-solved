/*
1. First attempt: Sort by height then iterate pair-by-pair -> time limit exceeded (O(n^2))
2. Second attempt: Start from the widest width and shorten it step by step
3. In order to contain more water than the widest-width-case, the newly selected line must be higher
*/
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;

        int max_amount = -1;
        while (left < right) {
            max_amount = max(max_amount, (right - left) * min(height[left], height[right]));
            if (height[left] < height[right]) { left++; }
            else { right--; }
        }

        return max_amount;
    }
};
