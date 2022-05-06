#include <vector>

using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid[0][0] == 1) { return 0; }
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();

        vector<vector<int>> paths;
        vector<int> first_row;
        bool obstacle_exists = false;
        for (int i = 0; i < n; i++) {
            if (obstacleGrid[0][i] == 1) { obstacle_exists = true; }
            if (!obstacle_exists) { first_row.push_back(1); }
            else { first_row.push_back(0); }
        }
        paths.push_back(first_row);
        obstacle_exists = false;
        for (int i = 1; i < m; i++) {
            vector<int> row;
            if (obstacleGrid[i][0] == 1) { obstacle_exists = true; }
            if (!obstacle_exists) { row.push_back(1); }
            else { row.push_back(0); }
            for (int j = 1; j < n; j++ ) { row.push_back(0); }
            paths.push_back(row);
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 1) { paths[i][j] = 0; }
                else {
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1];
                }
            }
        }

        return paths[m - 1][n - 1];
    }
};
