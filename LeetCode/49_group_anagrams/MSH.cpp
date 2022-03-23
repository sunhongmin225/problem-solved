// 1. Referring as map[key] will automatically assume that map has "key" with value of default(0)
// 2. First attempt (commented out): 1400ms (accepted but veeeery slow for C++..) but I don't think that this solution is that bad :/
// 3. Second attempt: Sort strings and use them as keys (Idea from: https://leetcode.com/problems/group-anagrams/discuss/19200/C%2B%2B-unordered_map-and-counting-sort)

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> answer;
        if (strs.size() <= 1) { answer.push_back(strs); return answer; }

        unordered_map<string, vector<string>> umap;
        for (int i = 0; i < strs.size(); i++) {
            string target = strs[i];
            sort(target.begin(), target.end());
            umap[target].push_back(strs[i]);
        }

        unordered_map<string, vector<string>>::iterator iter;
        for (iter = umap.begin(); iter != umap.end(); iter++) {
            answer.push_back(iter->second);
        }
        return answer;
    }

    /*
    void increment_frequency (unordered_map<char, int> &umap, char c) {
        if (umap.find(c) == umap.end()) { umap[c] = 1; }
        else { umap[c]++; }
    }

    bool equals (unordered_map<char, int> &umap1, unordered_map<char, int> &umap2) {
        if (umap1.size() != umap2.size()) { return false; }
        unordered_map<char, int>::iterator iter1;
        for (iter1 = umap1.begin(); iter1 != umap1.end(); iter1++) {
            if (umap2.find(iter1->first) == umap2.end()) { return false; }
            else if (iter1->second != umap2[iter1->first]) { return false; }
        }
        return true;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> answer;
        if (strs.size() <= 1) { answer.push_back(strs); return answer; }

        vector<unordered_map<char, int>> umaps;
        for (int i = 0; i < strs.size(); i++) {
            string target = strs[i];
            unordered_map<char, int> umap;
            for (int j = 0; j < target.size(); j++) {
                increment_frequency(umap, target.at(j));
            }
            umaps.push_back(umap);
        }

        vector<bool> board;
        for (int i = 0; i < strs.size(); i++) {
            board.push_back(false);
        }

        for (int i = 0; i < umaps.size() - 1; i++) {
            if (board[i]) { continue; }
            vector<string> ans;
            ans.push_back(strs[i]);
            board[i] = true;
            for (int j = i + 1; j < umaps.size(); j++) {
                if (board[j]) { continue; }
                if (equals(umaps[i], umaps[j])) {
                    ans.push_back(strs[j]);
                    board[j] = true;
                }
            }
            answer.push_back(ans);
        }

        if (!board[strs.size() - 1]) {
            vector<string> ans;
            ans.push_back(strs[strs.size() - 1]);
            answer.push_back(ans);
        }

        return answer;
    }
    */
};
