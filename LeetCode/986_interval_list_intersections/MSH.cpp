/*
1. Focused on reducing (covering) edge cases by using more general conditions
2. Tried to avoid redundancy by returning indicator variables
*/
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> overlapped_intervals (vector<int>& first, vector<int>& second) {
        vector<int> answer;
        if (first[1] < second[0]) {
            answer.push_back(0);
            answer.push_back(-1); // indicator variable to tell you that first_finger should be moved
            return answer;
        } else if (second[1] < first[0]) {
            answer.push_back(0);
            answer.push_back(-2); // indicator variable to tell you that second_finger should be moved
            return answer;
        }

        if (second[0] <= first[1] || first[0] <= second[1]) {
            answer.push_back(max(first[0], second[0]));
            answer.push_back(min(first[1], second[1]));
            return answer;
        }

        return answer; // should not reach here
    }

    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        int first_size = firstList.size();
        int second_size = secondList.size();
        int first_finger = 0;
        int second_finger = 0;
        vector<vector<int>> answer;

        while (true) {
            if (first_finger == first_size || second_finger == second_size) { break; }
            vector<int> candidate = overlapped_intervals (firstList[first_finger], secondList[second_finger]);
            if (candidate[1] == -1) { first_finger++; }
            else if (candidate[1] == -2) { second_finger++; }
            else {
                if (firstList[first_finger][1] < secondList[second_finger][1]) { first_finger++; }
                else { second_finger++; }
                answer.push_back(candidate);
            }
        }

        return answer;
    }
};
