#include <vector>

using namespace std;
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int max_val = *max_element(nums.begin(), nums.end()); // max_element returns an iterator
        vector<int> dp(max_val + 1, 0); // dp[i]: (assume that nums is sorted) max earnable points if points (i.e., elements of nums) are used up to point i

        for (int num : nums) { dp[num] += num; } // for redundant points, they can all be used

        for (int i = 2; i <= max_val; i++) {
            dp[i] = max(dp[i - 1], dp[i - 2] + dp[i]); // if point i - 1 is used then point i(s) are deleted; if point i is used it indicates that point i - 2 was also used (i.e., greedy)
        }

        return dp[max_val];
    }
};
