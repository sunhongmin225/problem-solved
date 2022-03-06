#include <vector>

using namespace std;

class Solution {
public:
    void restore (vector<int>& orig, vector<int>& copy) {
        copy.clear();
        for (int i = 0; i < orig.size(); i++) { copy.push_back(orig[i]); }
    }

    void add_permutation (vector<vector<int>> &answers, vector<int>& nums, vector<int>& ans) {
        if (nums.size() == 0) { answers.push_back(ans); } // no more entries left so add to answers

        vector<int> nums_copy;
        for (int i = 0; i < nums.size(); i++) { nums_copy.push_back(nums[i]); }

        vector<int> ans_copy;
        for (int i = 0; i < ans.size(); i++) { ans_copy.push_back(ans[i]); }

        for (int i = 0; i < nums.size(); i++) {
            ans.push_back(nums[i]);
            nums_copy.erase(nums_copy.begin() + i);
            add_permutation (answers, nums_copy, ans);
            restore (nums, nums_copy);
            restore (ans_copy, ans);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> answers;
        vector<int> nums_copy;
        for (int i = 0; i < nums.size(); i++) { nums_copy.push_back(nums[i]); }

        for (int i = 0; i < nums.size(); i++) {
            vector<int> ans;
            ans.push_back(nums[i]);
            nums_copy.erase(nums_copy.begin() + i); // erase ith element before adding permutation
            add_permutation (answers, nums_copy, ans);
            restore (nums, nums_copy); // restore nums_copy before next iteration
        }
        return answers;
    }
};
