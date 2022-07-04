/*
1. Searched for usage of reverse() and resize() in vector
*/
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void rotate (vector<int>& nums, int k) {
        if (k == 0 || nums.size() == 1) { return; }

        reverse(nums.begin(), nums.end());

        int idx = 0;
        while (true) {
            nums.push_back(nums[idx++]);
            if (idx == k) { break; }
        }

        reverse(nums.begin(), nums.end());
        nums.resize(nums.size() - k);

        return;
    }

};
