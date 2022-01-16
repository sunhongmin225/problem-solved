/*
1. binary_to_decimal and decimal_to_binary are handy methods
2. C++ innate sort algorithm is not so expensive! O(nlogn)
3. Hint from problem description: may return any of multiple answers -> return right away if possible
*/
#include <string>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    // only need to scan string binary once
    int binary_to_decimal (string binary) {
        int n = binary.length();
        int answer = 0;
        for (int i = 0; i < n; i++) {
            answer += pow(2, i) * (binary.at(n - 1 - i) - '0');
        }
        return answer;
    }

    // only need to perform division log(decimal) times
    string decimal_to_binary (int decimal, int n) {
        string answer;
        while (decimal != 0) {
            answer = (decimal % 2 == 0 ? "0" : "1") + answer;
            decimal /= 2;
        }

        int answer_length = answer.length();
        if (decimal == 0) {
            for (int i = 0; i < n - answer_length; i++) { answer = "0" + answer; }
        }
        return answer;
    }

    string findDifferentBinaryString(vector<string>& nums) {

        int n = nums.size();
        sort(nums.begin(), nums.end()); // O(nlogn)

        vector<int> nums_decimal;
        // iterate n times
        for (string num : nums) {
            nums_decimal.push_back(binary_to_decimal(num));
        }

        int sequence = 0;
        // iterate n times
        for (int num_decimal : nums_decimal) {
            if (num_decimal == sequence) {
                sequence++;
                continue;
            } else {
                return decimal_to_binary(sequence, n);
            }
        }

        return decimal_to_binary(nums_decimal[n - 1] + 1, n);
    }
};
