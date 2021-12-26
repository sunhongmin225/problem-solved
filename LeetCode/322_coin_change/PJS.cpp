#include <algorithm>
#include <limits>
#include <vector>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount <= 0) {
            return 0;
        }
        
        if (coins.size() == 1 && amount % coins[0] == 0) {
            return amount / coins[0];
        }
        
        vector<int> num_min_coins;

        for (int partial_sum = 0 ; partial_sum < amount+1 ; partial_sum++) {
            num_min_coins.push_back(INT_MAX);
            for (auto coin : coins) {
                
                if (coin == partial_sum) {
                    num_min_coins[partial_sum] = 1;
                    continue;
                }
                
                int amount_before_adding = partial_sum - coin;
                if (amount_before_adding < 0) {
                    continue;
                } else {
                    int num_coins_before_adding = num_min_coins[amount_before_adding];
                    if (num_coins_before_adding < INT_MAX) {
                        num_min_coins[partial_sum] = min(num_min_coins[partial_sum], num_coins_before_adding + 1);
                    }
                }
            }
        }
        if (num_min_coins[amount] == INT_MAX) {
            return -1;
        } else {
            return num_min_coins[amount];
        }
    }
};
