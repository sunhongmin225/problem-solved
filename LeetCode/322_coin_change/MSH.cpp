class Solution {
public:

    int coinChange(vector<int>& coins, int amount) {

        vector<int> scoreboard;
        scoreboard.reserve(amount + 1);
        scoreboard.push_back(0);

        for (int i = 1; i < amount + 1; i++) {
            scoreboard.push_back(amount + 1);
        }

        for (int i = 1; i < amount + 1; i++) {
            for (int j = 0; j < coins.size(); j++) {
                if (coins[j] <= i) {
                    int partial = scoreboard[i - coins[j]];
                    if (partial + 1 < scoreboard[i]) {
                        scoreboard[i] = partial + 1;
                    }
                }
            }
        }

        if (scoreboard[amount] == amount + 1)
            return -1;

        return scoreboard[amount];
    }
};