/*
1. Searched for map related grammars (e.g., find, iterator)
2. First attempt: find sequence candidates and search for their frequency again (> two scans)
3. Second attempt: directly add sequence candidates to map and count (can finish at one scan)
*/
#include <string>
#include <vector>
#include <map>

#define TARGET_NUM 10

using namespace std;

class Solution {
public:
    void insert_if_not_present (map<string, int> &sequence_map, string sequence) {
        if (sequence_map.find(sequence) == sequence_map.end() ) {
            sequence_map[sequence] = 1;
        } else {
            sequence_map[sequence] += 1;
        }
    }

    vector<string> findRepeatedDnaSequences (string s) {

        if (s.length() <= TARGET_NUM) { vector<string> empty_vector; return empty_vector; }

        map<string, int> sequence_map;
        for (int i = 0; i <= s.length() - TARGET_NUM; i++) {
            string sequence = s.substr(i, TARGET_NUM);
            insert_if_not_present(sequence_map, sequence);
        }

        vector<string> answer;
        auto iter = sequence_map.begin();
        while (iter != sequence_map.end()) {
            if (iter->second > 1) { answer.push_back(iter->first); }
            iter++;
        }

        return answer;
    }
};
