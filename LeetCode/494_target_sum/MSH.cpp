// 1. Backtracking: Time limit exceeded
// 2. I know that it's a DP but can't solve it :(
#include <vector>

using namespace std;

class Solution {
public:
    int my_find_target_sum_ways (vector<int>& nums, int target) {
        if (nums.size() > 1) {
            int new_target_smaller = target - nums[nums.size() - 1];
            int new_target_bigger  = target + nums[nums.size() - 1];
            vector<int> new_nums;
            for (int i = 0; i < nums.size() - 1; i++) { new_nums.push_back(nums[i]); }
            return my_find_target_sum_ways(new_nums, new_target_smaller) + my_find_target_sum_ways(new_nums, new_target_bigger);
        } else {
            if (nums[0] == target && (-1) * nums[0] == target) { return 2; }
            else if (nums[0] == target || (-1) * nums[0] == target) { return 1; }
            else return 0;
        }
    }

    int findTargetSumWays(vector<int>& nums, int target) {
        return my_find_target_sum_ways(nums, target);
    }
};
