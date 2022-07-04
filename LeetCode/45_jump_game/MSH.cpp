#include <vector>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int dp[nums.size() + 1];
        dp[0] = 0;
        dp[1] = 0;

        for (int i = 2; i <= nums.size(); i++) {
            int min = i - 1;
            if (nums[i - 1] > 0) {
                dp[i] = dp[i - 1] + 1;
                min = dp[i - 1] + 1;
            }

            for (int j = 0; j < i - 1; j++) {
                if (nums[j] + j >= i - 1) {
                    if (dp[j + 1] + 1 < min) { min = dp[j + 1] + 1; }
                    dp[i] = min;
                }
            }
        }

        return dp[nums.size()];
    }
};
