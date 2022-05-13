#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int numSquares(int n) {
        int sqrt_n = sqrt(n);
        if (n == sqrt_n * sqrt_n) { return 1; }
        vector<int> dp(n + 1, 0); // dp[i]: the least number of PSN that sum to i

        for (int i = 0; i < dp.size(); i++) { dp[i] = i; } // initialize with max number of PSN

        for (int i = 2; i < dp.size(); i++) {
            int sqrt_i = sqrt(i);
            if (i == sqrt_i * sqrt_i) { dp[i] = 1; }
            else {
                int min = i;
                for (int j = 1; j <= sqrt_i; j++) {
                    if (dp[i - j * j] + 1 < min) { min = dp[i - j * j] + 1; }
                }
                dp[i] = min;
            }
        }
        return dp[n];
    }
};
