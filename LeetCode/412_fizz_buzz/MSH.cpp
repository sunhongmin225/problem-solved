#include <string>
#include <vector>

#define FIZZ 3
#define BUZZ 5

using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {

        vector<string> answer;
        answer.reserve(n);

        for (int idx = 0; idx < n; idx++) {
            int effective_idx = idx + 1;
            if (effective_idx % (FIZZ * BUZZ) == 0) { answer.push_back("FizzBuzz"); }
            else if (effective_idx % FIZZ == 0) { answer.push_back("Fizz"); }
            else if (effective_idx % BUZZ == 0) { answer.push_back("Buzz"); }
            else { answer.push_back(to_string(effective_idx)); }
        }

        return answer;
    }
};
