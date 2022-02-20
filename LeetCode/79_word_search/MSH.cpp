/*
1. First attempt: BFS using queue -> difficult to implement backtracking
2. Second attempt: DFS using stack -> could not implement spending more than an hour :/
3. Third attempt: Reference - https://leetcode.com/problems/word-search/discuss/27835/C%2B%2B-dfs-solution.
*/
#include <vector>
#include <string>

using namespace std;

class Solution {
public:

    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size(); // board[0] always exists since 1 <= m
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (dfs(board, i, j, word)) { return true; }
        return false;
    }

    bool dfs(vector<vector<char>>& board, int i, int j, string& word) {
        if (word.length() == 0) { return true; }
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != word[0]) { return false; }
        char c = board[i][j];
        board[i][j] = '0'; // dummy character to rule out possibility of re-visiting board elements
        string s = word.substr(1); // leave out first char of word
        bool ret = dfs(board, i-1, j, s) || dfs(board, i+1, j, s) || dfs(board, i, j-1, s) || dfs(board, i, j+1, s);
        board[i][j] = c; // revert board into original status for other routes
        return ret;
    }

};
