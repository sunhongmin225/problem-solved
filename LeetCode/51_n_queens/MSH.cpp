/*
1. Reference: Ch. 5 Recursion from Data Structure Lecture by Prof. Byung-Ro Moon, SNU
2. Searched for usage of string.find() (cheat sheet needed..)
*/
#include <string>
#include <vector>

using namespace std;

class Solution {
public:

    void set_queen (int row, int col, vector<string> &chessboard) { chessboard[row][col] = 'Q'; }

    void remove_queen (int row, int col, vector<string> &chessboard) { chessboard[row][col] = '.'; }

    bool is_under_attack (int row, int col, vector<string> &chessboard) {
        int offset = 1;
        while (true) {
            if (row - offset < 0 || col - offset < 0) { break; }
            if (chessboard[row - offset][col - offset] == 'Q') { return true; } // queen exists in the upper-left diagonal
            offset++;
        }
        offset = 1;
        while (true) {
            if (row - offset < 0 || col + offset >= chessboard.size()) { break; }
            if (chessboard[row - offset][col + offset] == 'Q') { return true; } // queen exists in the upper-right diagonal
            offset++;
        }
        offset = 1;
        while (true) {
            if (row + offset >= chessboard.size() || col - offset < 0) { break; }
            if (chessboard[row + offset][col - offset] == 'Q') { return true; } // queen exists in the lower-left diagonal
            offset++;
        }
        offset = 1;
        while (true) {
            if (row + offset >= chessboard.size() || col + offset >= chessboard.size()) { break; }
            if (chessboard[row + offset][col + offset] == 'Q') { return true; } // queen exists in the lower-right diagonal
            offset++;
        }
        if (chessboard[row].find('Q') != string::npos) { return true; } // queen exists in the same row
        for (int i = 0; i < chessboard.size(); i++) {
            if (chessboard[i][col] == 'Q') { return true; } // queen exists in the same column
        }
        return false;
    }

    // assumption: queens are correctly placed in columns 0 to max(0, col - 1)
    void place_queens (int col, vector<string> &chessboard, vector<vector<string>> &answer) {
        if (col >= chessboard.size()) { answer.push_back(chessboard); return; }
        else {
            for (int row = 0; row < chessboard.size(); row++) {
                if (!is_under_attack(row, col, chessboard)) {
                    set_queen(row, col, chessboard);
                    place_queens(col + 1, chessboard, answer);
                    remove_queen(row, col, chessboard);
                }
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {

        vector<vector<string>> answer;
        vector<string> chessboard;
        string empty_row = "";
        for (int i = 0; i < n; i++) { empty_row += "."; }
        for (int i = 0; i < n; i ++) {
            chessboard.push_back(empty_row);
        }

        if (n == 1) {
            set_queen(0, 0, chessboard);
            answer.push_back(chessboard);
            return answer;
        }

        place_queens (0, chessboard, answer);

        return answer;
    }
};
