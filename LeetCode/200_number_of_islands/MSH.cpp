/*
1. Try to implement exactly as what you've 'pictured'.
2. Boundary check is important.
*/
#include <vector>

using namespace std;

class Solution {
public:

    void sink(vector<vector<char>>& grid, int p, int q) {
        // handle edge cases
        if (p < 0 || p >= grid.size() || q < 0 || q >= grid[0].size())
            return;
        // no need to sink if it is already water
        if (grid[p][q] == '0')
            return;

        // sink current location
        grid[p][q] = '0';
        // sink horizontally and vertically
        sink(grid, p - 1, q);
        sink(grid, p + 1, q);
        sink(grid, p, q - 1);
        sink(grid, p, q + 1);
    }

    int numIslands(vector<vector<char>>& grid) {

        int answer = 0;
        int m = grid.size();
        int n = grid[0].size(); // m >= 1 so grid[0] always exists

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // bumped into a land
                if (grid[i][j] == '1') {
                    answer++;
                    sink(grid, i, j);
                }
            }
        }

        return answer;
    }
};