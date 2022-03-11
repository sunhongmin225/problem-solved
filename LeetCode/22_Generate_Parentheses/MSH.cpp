#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    void generate_parantheses (vector<string> &strings, string s, int num_left_paranthesis_used, int num_right_paranthesis_used, int n) {
        if (s.size() == 0) { // base case where string s is empty("")
            s += "(";
            generate_parantheses (strings, s, 1, 0, n);
            return;
        }
        
        if (s.size() == 2 * n) { // parantheses generation has ended
            strings.push_back(s);
            return;
        }
        
        if (num_left_paranthesis_used == n) { // no more left_paranthesis remaining so concat right_paranthesis
            s += ")";
            generate_parantheses (strings, s, num_left_paranthesis_used, num_right_paranthesis_used + 1, n);
            return;
        }
        
        if (num_left_paranthesis_used == num_right_paranthesis_used) { // only option is to concat left_paranthesis to make well-formed parantheses
            s += "(";
            generate_parantheses (strings, s, num_left_paranthesis_used + 1, num_right_paranthesis_used, n);
            return;
        }
        
        if (n - num_left_paranthesis_used == 1 && n - num_right_paranthesis_used == 1) { // last remaining left_paranthesis must precede right_paranthesis to make well-formed parantheses
            s += "(";
            generate_parantheses (strings, s, num_left_paranthesis_used + 1, num_right_paranthesis_used, n);            
            return;
        }
        
        // if all the conditions listed above do not meet, it is possible to concat either left_paranthesis or right_paranthesis
        generate_parantheses (strings, s + "(", num_left_paranthesis_used + 1, num_right_paranthesis_used, n);
        generate_parantheses (strings, s + ")", num_left_paranthesis_used, num_right_paranthesis_used + 1, n);
        return;        
    }
    
    vector<string> generateParenthesis (int n) {
        vector<string> answer;
        generate_parantheses(answer, "", 0, 0, n);
        return answer;
    }
};
