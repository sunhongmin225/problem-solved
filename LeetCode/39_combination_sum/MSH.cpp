// reference: https://leetcode.com/problems/combination-sum/discuss/16496/Accepted-16ms-c%2B%2B-solution-use-backtracking-easy-understand.

#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int> > res;
        vector<int> combination;
        combinationSum(candidates, target, res, combination, 0);
        return res;
    }

    void combinationSum(vector<int> &candidates, int target, vector<vector<int> > &res, vector<int> &combination, int begin) {
        if (target == 0) {
            res.push_back(combination);
            return;
        }
        for (int i = begin; i != candidates.size() && target >= candidates[i]; i++) {
            combination.push_back(candidates[i]);
            combinationSum(candidates, target - candidates[i], res, combination, i);
            combination.pop_back();
        }
    }
};
