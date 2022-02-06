/*
1. Inferior solution (lower 7th percentile runtime, 5th percentile memory)
*/
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:

    bool exists (unordered_set<string> &set, vector<string> elements) {
        for (int i = 0; i < elements.size(); i++) {
            if (set.find(elements[i]) != set.end()) { continue; }
            else { return false; }
        }
        return true;
    }

    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {

        int n = recipes.size();
        unordered_set<string> supplies_set;
        for (int i = 0; i < supplies.size(); i++) { supplies_set.insert(supplies[i]); }

        vector<int> answer_idx;
        bool state_change;
        while (true) {
            state_change = false;
            for (int i = 0; i < n; i++) {
                if (find(answer_idx.begin(), answer_idx.end(), i) != answer_idx.end()) { continue; }
                if (exists(supplies_set, ingredients[i])) {
                    state_change = true;
                    answer_idx.push_back(i);
                    supplies_set.insert(recipes[i]);
                }
            }
            if (!state_change) { break; }
        }

        vector<string> answer;
        for (int i = 0; i < answer_idx.size(); i++) {
            answer.push_back(recipes[answer_idx[i]]);
        }

        return answer;
    }
};
