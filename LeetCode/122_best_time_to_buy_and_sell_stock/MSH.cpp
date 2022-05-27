#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int days = prices.size();
        if (days == 1) { return 0; }
        vector<int> dp(days + 1, 0); // dp[i]: the maximum profit you can achieve until i-th day (day starts from 1; ignore i == 0)

        for (int i = 1; i < days; i++) {
            int profit = prices[i] - prices[i - 1];
            if (profit > 0) { dp[i + 1] = dp[i] + profit; }
            else { dp[i + 1] = dp[i]; }
        }

        return dp[days];
    }
};
