/*
1. Searched for the usage of exception. (C++ grammer-wise)
2. Take care of edge cases. (boundary conditions)
*/
#include <string>
#include <cmath>

using namespace std;

class Solution {
public:

    int reverse(int x) {

        if (x == 0) { return 0; }
        if (x == (- 1) * pow(2, 31)) { return 0; }

        bool is_negative = x < 0;
        if (is_negative) x = (- 1) * x;

        string x_str = to_string(x);

        for (int i = 0; i < x_str.length() / 2; i++) {
            char temp = x_str.at(i);
            x_str.at(i) = x_str.at(x_str.length() - 1 - i);
            x_str.at(x_str.length() - 1 - i) = temp;
        }

        int answer = 0;
        try {
            answer = stoi(x_str);
        } catch (const exception& e) {
            return 0;
        }

        if (is_negative) {
            return (- 1) * answer;
        } else {
            return answer;
        }

        return 0;
    }
};
