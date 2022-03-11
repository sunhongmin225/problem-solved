#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        double answer = 0;
        bool is_between = false; // true if median is between two elements (need to average)
        if ((m + n) % 2 == 0) { is_between = true; }
        int pos = (m + n) / 2; // if !is_between, pos is the position of median; if is_between, average of element in pos and pos - 1 is median

        // handle edge cases
        if (m == 0 || n == 0) {
            if (!is_between) {
                if (m == 0) { answer = nums2[pos]; }
                else { answer = nums1[pos]; }
            } else {
                if (m == 0) { answer = (nums2[pos - 1] + nums2[pos]) / 2.0; }
                else { answer = (nums1[pos - 1] + nums1[pos]) / 2.0; }
            }
            return answer;
        }

        int left_finger = 0; // left corresponds to nums1
        int right_finger = 0; // right corresponds to nums2
        int curr_pos = -1; // (virtual) current position of concatenated array
        bool is_left = false;

        while (true) {
            if (curr_pos == m + n - 1) { break; } // break if scanned until end of concatenated array (should not reach here)
            is_left = false; // whether to look at nums1 or not
            int left = 0;
            int right = 0;
            if (left_finger == nums1.size()) { left = nums1[left_finger - 1]; }
            else { left = nums1[left_finger]; }
            if (right_finger == nums2.size()) { right = nums2[right_finger - 1]; }
            else { right = nums2[right_finger]; }

            // move fingers appropriately
            if (left <= right) {
                if (left_finger == nums1.size()) { // left_finger no longer can be moved
                    curr_pos++;
                    right_finger++;
                } else {
                    is_left = true;
                    curr_pos++;
                    left_finger++;
                }
            } else {
                if (right_finger == nums2.size()) { // right_finger no longer can be moved
                    is_left = true;
                    curr_pos++;
                    left_finger++;
                } else {
                    curr_pos++;
                    right_finger++;
                }
            }

            // check if median (or ingredients of median) is found
            if (curr_pos == pos && !is_between) { // median is found
                if (is_left) { answer = nums1[left_finger - 1]; }
                else { answer = nums2[right_finger - 1]; }
                return answer;
            } else if (curr_pos == pos - 1 && is_between) { // first element of ingredients of median
                if (is_left) { answer += nums1[left_finger - 1]; }
                else { answer += nums2[right_finger - 1]; }
            } else if (curr_pos == pos && is_between) { // second(last) element of ingredients of median
                if (is_left) { answer += nums1[left_finger - 1]; }
                else { answer += nums2[right_finger - 1]; }
                return answer / 2.0;
            }
        }

        return answer; // should not reach here
    }
};
