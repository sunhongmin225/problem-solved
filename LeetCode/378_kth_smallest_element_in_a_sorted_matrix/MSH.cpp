/*
1. There is a hint: each of the rows and columns is sorted in ascending order => need to wisely use the hint
*/
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {

        int n = matrix.size();
        if (n == 1) { return matrix[0][0]; } // handle an edge case

        vector<int> fingers;
        for (int i = 0; i < n; i++) { fingers.push_back(-1); }

        vector<int> partially_sorted_list;

        while (true) {
            int curr_max = matrix[n - 1][fingers[n - 1] + 1]; // safe since each row and column is sorted in ascending order
            for (int i = 0; i < n; i++) {
                while (true) {
                    if (fingers[i] + 1 == n) { break; }
                    if (matrix[i][fingers[i] + 1] <= curr_max) {
                        fingers[i]++;
                        partially_sorted_list.push_back(matrix[i][fingers[i]]);
                    } else { break; }
                }
            }
            if (k <= partially_sorted_list.size()) { break; } // kth element exists in partially_sorted_list
            else { k-= partially_sorted_list.size(); partially_sorted_list.clear(); } // need to scan more
        }

        sort(partially_sorted_list.begin(), partially_sorted_list.end());
        return partially_sorted_list[k -1];

    }
};
