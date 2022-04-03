#include <vector>

using namespace std;

class Solution {
public:
    struct row {
        int id;
        int num_soldiers;
    };

    static bool is_weaker (row a, row b) {
        if (a.num_soldiers < b.num_soldiers) { return true; }
        else if (a.num_soldiers == b.num_soldiers && a.id < b.id) { return true; }
        else { return false; }
    }

    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();

        vector<row> rows;
        for (int i = 0; i < m; i++) {
            rows.push_back(row());
            rows[i].id = i;
            int num_soldiers = 0;
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) { num_soldiers++; }
            }
            rows[i].num_soldiers = num_soldiers;
        }

        sort(rows.begin(), rows.end(), is_weaker);

        vector<int> ans;
        for (int i = 0; i < k; i++) {
            ans.push_back(rows[i].id);
        }

        return ans;
    }
};
