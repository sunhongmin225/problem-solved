/*
1. Pay attention to the condition that births and deaths occur "simultaenously"
*/
#include <vector>

using namespace std;

class Solution {
public:
    int num_of_alive_neighbors (vector<vector<int>>& board, int x, int y) {
        int m = board.size();
        int n = board[0].size();
        int answer = 0;

        if (x - 1 >= 0 && y - 1 >= 0 && board[x - 1][y - 1] == 1) { answer++; }
        if (x - 1 >= 0 && board[x - 1][y] == 1) { answer++; }
        if (x - 1 >= 0 && y + 1 < n && board[x - 1][y + 1] == 1) { answer++; }
        if (y - 1 >= 0 && board[x][y - 1] == 1) { answer++; }
        if (y + 1 < n && board[x][y + 1] == 1) { answer++; }
        if (x + 1 < m && y - 1 >= 0 && board[x + 1][y - 1] == 1) { answer++; }
        if (x + 1 < m && board[x + 1][y] == 1) { answer++; }
        if (x + 1 < m && y + 1 < n && board[x + 1][y + 1] == 1) { answer++; }

        return answer;
    }

    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        vector<vector<int>> cells_to_be_dead;
        vector<vector<int>> cells_to_be_alive;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int nums = num_of_alive_neighbors(board, i, j);
                if (board[i][j] == 1) { // live cell
                    if (nums < 2 || nums > 3) {
                        vector<int> pos;
                        pos.push_back(i);
                        pos.push_back(j);
                        cells_to_be_dead.push_back(pos);
                    }
                } else { // dead cell
                    if (nums == 3) {
                        vector<int> pos;
                        pos.push_back(i);
                        pos.push_back(j);
                        cells_to_be_alive.push_back(pos);
                    }
                }
            }
        }

        for (int i = 0; i < cells_to_be_dead.size(); i++) {
            board[cells_to_be_dead[i][0]][cells_to_be_dead[i][1]] = 0;
        }
        for (int i = 0; i < cells_to_be_alive.size(); i++) {
            board[cells_to_be_alive[i][0]][cells_to_be_alive[i][1]] = 1;
        }

    }
};
