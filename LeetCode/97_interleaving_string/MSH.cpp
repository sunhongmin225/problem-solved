// 1st attempt: Tried to implement with DP but couldn't.
// 2nd attempt: Backtracking using DFS but time limit exceeded.
// 3rd attempt: Reference from https://leetcode.com/problems/interleaving-string/discuss/31879/My-DP-solution-in-C%2B%2B
#include <string>

using namespace std;

class Solution {
public:
    bool isInterleave (string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size()) { return false; }
        bool dp[s1.size() + 1][s2.size() + 1]; // dp[i][j]: true if s3 until (i+j)th element can be represented as interleaving string of s1 until ith element and s2 until jth element
        for (int i = 0; i < s1.size() + 1; i++) {
            for (int j = 0; j < s2.size() + 1; j++) {
                dp[i][j] = false;
            }
        }

        for (int i = 0; i < s1.size() + 1; i++) {
            for (int j = 0; j < s2.size() + 1; j++) {
                if (i == 0 && j == 0) { dp[i][j] = true; }
                else if (i == 0) { dp[i][j] = (dp[i][j - 1] && s2.at(j - 1) == s3.at(i + j - 1)); }
                else if (j == 0) { dp[i][j] = (dp[i - 1][j] && s1.at(i - 1) == s3.at(i + j - 1)); }
                else {
                    dp[i][j] = (dp[i][j - 1] && s2.at(j - 1) == s3.at(i + j - 1)) || (dp[i - 1][j] && s1.at(i - 1) == s3.at(i + j - 1));
                }
            }
        }

        return dp[s1.size()][s2.size()];
    }
};
