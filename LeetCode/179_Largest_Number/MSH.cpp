/*
1. Need to handle special cases, e.g., 43243 432, 0 0
2. When writing compare function, return right away when two instances are equal
*/
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    static bool my_compare (const string &a, const string &b) {
        int shorter_length = min(a.size(), b.size());
        for (int i = 0; i < shorter_length; i++) {
            if (a.at(i) > b.at(i)) { return true; }
            else if (a.at(i) < b.at(i)) { return false; }
        }

        if (a.size() < b.size()) {
            return my_compare(a, b.substr(a.size()));
        } else if (a.size() > b.size()) {
            return my_compare(a.substr(b.size()), a);
        } else {
            return false; // if this is set to true, error is returned for special cases (e.g., nums = [0] * 17) (I don't know why)
        }
    }

    string largestNumber(vector<int>& nums) {
        // convert vector<int> nums to vector<string> nums_str
        vector<string> nums_str;
        for (int i = 0; i < nums.size(); i++) { nums_str.push_back(to_string(nums[i])); }

        // sort nums_str by my_compare criterion
        sort(nums_str.begin(), nums_str.end(), my_compare);

        // concat nums_str to ans
        string ans = "";
        for (int i = 0; i < nums_str.size(); i++) { ans += nums_str[i]; }

        // handle cases when multiple zero precede
        int start_idx = 0;
        for (int i = 0; i < ans.size() - 1; i++) {
            if (ans.at(i) == '0') { start_idx = i + 1; }
            else { break; }
        }

        return ans.substr(start_idx);
    }
};
