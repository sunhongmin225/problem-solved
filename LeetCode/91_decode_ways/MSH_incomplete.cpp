/*
1. My approach: Use unordered_set to record all trials -> valid but time limit exceeded
*/
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

struct Decoding {
    vector<int> elems;

    bool operator== (const Decoding& d) const {
        if (elems.size() != d.elems.size()) { return false; }
        for (int i = 0; i < elems.size(); i++) {
            if (elems[i] != d.elems[i]) { return false; }
        }
        return true;
    }

};

class MyHashFunction {
public:
    size_t operator() (const Decoding& d) const {
        size_t val = 0;
        for (int i = 0; i < d.elems.size(); i++) {
            val *= d.elems[i];
        }
        return val;
    }
};

class Solution {
public:

    static bool trial (vector<int>& msg, int idx, vector<int> elems, unordered_set<Decoding, MyHashFunction>& uset) {
        if (idx >= msg.size() - 1) {
            Decoding d;
            d.elems = elems;
            uset.insert(d);
            return false;
        }
        if (msg[idx] != 1 && msg[idx] != 2) {
            return trial (msg, idx + 1, elems, uset);
        }
        if (msg[idx] == 2 && msg[idx + 1] >= 7) {
            return trial (msg, idx + 2, elems, uset);
        } else if (msg[idx + 1] >= 10) {
            return trial (msg, idx + 2, elems, uset);
        }
        if (msg[idx + 1] == 1 || msg[idx + 1] == 2)
            trial (msg, idx + 1, elems, uset);
        elems.push_back(idx);
        Decoding d;
        d.elems = elems;
        uset.insert(d);
        return trial (msg, idx + 2, elems, uset);
    }

    int numDecodings(string s) {
        if (s.at(0) == '0') { return 0; }
        vector<int> base;

        for (int i = 0; i < s.size(); i++) {
            if (s.at(i) == '0') {
                if (s.at(i - 1) != '1' && s.at(i - 1) != '2') { return 0; }
                else {
                    base.erase(base.end() - 1);
                    base.push_back((s.at(i - 1) - '0') * 10);
                    continue;
                }
            }
            base.push_back(s.at(i) - '0');
        }

        unordered_set<Decoding, MyHashFunction> uset;

        for (int i = 0; i < base.size(); i++) {
            vector<int> elems;
            trial (base, i, elems, uset);
        }

        int offset = 0;
        auto iter = unordered_set<Decoding, MyHashFunction>::iterator();
        int idx = 0;
        for (iter = uset.begin(); iter != uset.end(); iter++) {
            if ((*iter).elems.size() == 0) { offset = -1; }
        }

        return uset.size() + 1 + offset;

    }
};
