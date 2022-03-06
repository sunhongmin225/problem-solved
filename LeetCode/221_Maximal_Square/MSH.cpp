/*
1. First attempt: direct counting -> time limit exceeds
2. Second attempt: DP -> still slow (lower 5% percentile) but is accepted
*/
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    // return true if zero exists in righter-most column and lower-most row
    static bool zero_exists (vector<vector<char>>& matrix, int x, int y, int width) {
        for (int i = 0; i < width; i++) {
            if (matrix[x + i][y + width - 1] == '0') { return true; }
        }
        for (int i = 0; i < width - 1; i++) {
            if (matrix[x + width - 1][y + i] == '0') { return true; }
        }
        return false;
    }

    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size(); // matrix[0] always exists since 1 <= m
        int max_possible_ans = min(m, n);

        // board to save DP results
        vector<vector<unordered_set<int>>> board;

        // initialize board with dummy unordered set for concise access syntaxes
        for (int i = 0; i < m; i++) {
            vector<unordered_set<int>> board_row;
            unordered_set<int> dummy_set;
            for (int j = 0; j < n; j++) {
                board_row.push_back(dummy_set);
            }
            board.push_back(board_row);
        }

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int max_possible_ans = min(m - i, n - j);
                // no need to scan when max possible answer is smaller than or equal to answer
                if (max_possible_ans <= ans) { continue; }
                for (int width = 1; width <= max_possible_ans; width++) {
                    if (width == 1) { // base case
                        if (matrix[i][j] == '1') {
                            board[i][j].insert(1);
                            ans = max(ans, 1);
                        }
                    } else {
                        if (board[i][j].find(width - 1) != board[i][j].end()) {
                            // possible answer witnessed
                            if (!zero_exists(matrix, i, j, width)) {
                                board[i][j].insert(width);
                                ans = max(ans, width);
                            }
                        }
                    }
                }
            }
        }

        // return area of square
        return ans * ans;
    }

    /*
    static bool zero_exists (vector<vector<char>>& matrix, int x, int y, int width) {
        for (int i = x; i < x + width; i++) {
            for (int j = y; j < y + width; j++) {
                if (matrix[i][j] == '0') { return true; }
            }
        }
        return false;
    }

    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size(); // matrix[0] always exists since 1 <= m
        int max_possible_ans = min(m, n);

        for (int ans = max_possible_ans; ans > 0; ans--) {
            for (int i = 0; i <= m - ans; i++) {
                for (int j = 0; j <= n - ans; j++) {
                    if (!zero_exists(matrix, i, j, ans)) { return ans * ans; }
                }
            }
        }

        return 0;
    }
    */
};
