/*
1. First attempt: O(n^2) (precisely n^2/2) (not so efficient but since n is small(<1000), it may work)
2. First attempt works, but could there be better solution?
*/
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    static void add_if_not_exists (unordered_map<int, vector<pair<int, int>>> &board, int key, pair<int, int> val) {
        if (board.find(key) != board.end()) {
            board[key].push_back(val);
        } else {
            vector<pair<int, int>> to_push_back;
            to_push_back.push_back(val);
            board[key] = to_push_back;
        }
    }

    int tupleSameProduct(vector<int>& nums) {
        if (nums.size() < 4) { return 0; }

        // key is the multiplied value, and value is the vector of pairs whose product equals to the key
        unordered_map<int, vector<pair<int, int>>> board;

        // iterate for every pair (O(n^2/2))
        for (int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                int mult = nums[i] * nums[j];
                add_if_not_exists(board, mult, make_pair(nums[i], nums[j]));
            }
        }

        int answer = 0;
        auto iter = board.begin();
        while (iter != board.end()) {
            int n = iter->second.size();
            if (n > 1) {
                // 8 since there are 2 * 2 * 2 possible combinations of a * b = c * d
                // n choose 2 (nC2) since two pairs are chosen from n pairs
                answer += 8 * n * (n - 1) / 2;
            }
            iter++;
        }

        return answer;
    }
};
