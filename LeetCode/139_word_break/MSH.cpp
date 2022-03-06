/*
1. First attempt: O(n^2) brute-force method (backtracking) -> time limit exceeded
2. Second attempt: DP (reference: https://leetcode.com/problems/word-break/discuss/43814/C%2B%2B-Dynamic-Programming-simple-and-fast-solution-(4ms)-with-optimization)
3. Retrospect: It wasn't that difficult but I've searched for the solution too easily. Need to reflect on it.
*/
#include <string>
#include <unordered_set>
#include <vector>

#define MAX_WORD_LEN 20

using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {

        unordered_set<string> dict; // unordered_set for fast access
        for (int i = 0; i < wordDict.size(); i++) { dict.insert(wordDict[i]); }

        vector<bool> dp(s.length() + 1, false); // if dp[i] is true, it is possible to break s.substr(0, i) into words in dict
        dp[0] = true; // dummy entry

        for (int i = 1; i <= s.length(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (dp[j]) {
                    string word = s.substr(j, i - j);
                    if (dict.find(word) != dict.end()) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }

        return dp[s.length()];
    }

    // First attempt: O(n^2) brute-force method (backtracking) -> time limit exceeded
    /*
    bool exists(unordered_set<string>& dict, string key) {
        if (dict.find(key) != dict.end()) { return true; }
        else { return false; }
    }

    bool word_break (string& s, unordered_set<string>& dict) {

        vector<string> candidates;
        for (int len = 1; len <= min<int>(MAX_WORD_LEN, s.length()); len++) {
            if (exists(dict, s.substr(0, len))) { candidates.push_back(s.substr(0, len)); }
        }

        if (candidates.size() == 0) { return false; }

        for (int i = 0; i < candidates.size(); i++) {
            int len = candidates[i].length();
            string substr = s.substr(len);
            if (substr.length() == 0) { return true; }
            if (!word_break(substr, dict)) { continue; }
            else { return true; }
        }
        return false;
    }

    bool wordBreak(string s, vector<string>& wordDict) {

        unordered_set<string> dict;
        for (int i = 0; i < wordDict.size(); i++) { dict.insert(wordDict[i]); }

        return word_break(s, dict);

    }
    */
};
