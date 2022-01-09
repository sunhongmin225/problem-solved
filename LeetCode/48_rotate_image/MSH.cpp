/*
1. Drawing on the paper with small cases is useful.
2. At first I divided into cases where n % 2 == 0 and n % 2 == 1, but it turned out unnecessary. => I should try to cover as many cases as possible with a single method.
*/
#include <vector>

using namespace std;

class Solution {
public:

    void rotate(vector<vector<int>>& matrix) {

        int n = matrix.size();

        if (n == 1) { return; }
        for (int i = 0; i < (n + 1) / 2; i++) {
            int boundary = n - i * 2;
            if (boundary != 2 && boundary != 1) {
                for (int j = 0; j < boundary - 1; j++) {
                    int x = i;
                    int y = i + j;
                    int col_offset = n - 1;
                    int row_offset = n - 1 - 2 * i;
                    int temp = matrix[x][y];
                    matrix[x][y] = matrix[col_offset - y][x];
                    matrix[col_offset - y][x] = matrix[x + row_offset][col_offset - y];
                    matrix[x + row_offset][col_offset - y] = matrix[y][x + row_offset];
                    matrix[y][x + row_offset] = temp;
                }
            } else if (boundary == 2) {
                int x = i;
                int y = i;
                int temp = matrix[x][y];
                matrix[x][y] = matrix[x + 1][y];
                matrix[x + 1][y] = matrix[x + 1][y + 1];
                matrix[x + 1][y + 1] = matrix[x][y + 1];
                matrix[x][y + 1] = temp;
            }
        }
    }
};
