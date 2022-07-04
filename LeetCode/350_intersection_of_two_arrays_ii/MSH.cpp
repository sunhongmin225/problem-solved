// 1. First attempt: Direct comparison of all elements - time complexity is O(mn) which is inferior (but still passes)
// 2. Second attempt: Sort first (O(nlogn + mlogm)) then scan only once (O(max(m, n))) - much faster

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> common(vector<int> &shorter, vector<int> &longer) {
        vector<int> answer;

        int prev_j = 0;
        for (int i = 0; i < shorter.size(); i++) {
            for (int j = prev_j; j < longer.size(); j++) {
                if (longer[j] < shorter[i]) { continue; }
                else if (longer[j] == shorter[i]) { answer.push_back(shorter[i]); prev_j = j+1; break; }
                else if (longer[j] > shorter[i]) { prev_j = j; break; }
            }
        }
        return answer;
    }

    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> answer;

        sort(nums1.begin(), nums1.end()); // O(mlogm)
        sort(nums2.begin(), nums2.end()); // O(nlogn)

        if (nums1.size() < nums2.size()) { answer = common(nums1, nums2); } // O(n)
        else { answer = common(nums2, nums1); } // or O(m)

        return answer;
    }
};
