// 1. O(mn) seems to be the optimal
// 2. BFS does not work (time limit exceeded)

#include <vector>

using namespace std;

class Solution {
public:
    struct Block {
        int x;
        int y;
        int val;
        int sum;
    };

    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        // translate grid to Block-wise board
        vector<vector<Block>> board;
        for (int i = 0; i < m; i++) {
            vector<Block> row;
            for (int j = 0; j < n; j++) {
                row.push_back(Block());
                row[j].x = i;
                row[j].y = j;
                row[j].val = grid[i][j];
                row[j].sum = -1;
            }
            board.push_back(row);
        }

        board[0][0].sum = board[0][0].val;

        // fill out sum for each Block in first column and first row initially
        for (int i = 1; i < m; i++) { // first column
            board[i][0].sum = board[i - 1][0].sum + board[i][0].val;
        }
        for (int j = 1; j < n; j++) { // first row
            board[0][j].sum = board[0][j - 1].sum + board[0][j].val;
        }

        // check for upper & left Block's sum and choose the minimum
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                board[i][j].sum = min(board[i - 1][j].sum, board[i][j - 1].sum) + board[i][j].val;
            }
        }

        return board[m - 1][n - 1].sum;
    }
};
