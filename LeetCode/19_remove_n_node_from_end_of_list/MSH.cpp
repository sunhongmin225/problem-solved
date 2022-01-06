/*
1. Take care of edge cases. (where num_nodes == n)
2. I had to scan twice: first to find the length of the linked list, second to refer to correct position to delete => Can I do better at one scan?
3. I used two ListNode* to remember head => Can I do better, with one ListNode*?
*/

using namespace std;

/*
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        ListNode* original_head = head;

        int num_nodes = 1;
        while (head->next != nullptr) {
            head = head->next;
            num_nodes++;
        }

        if (num_nodes == n) { return original_head->next; }

        ListNode* answer = original_head;

        for (int i = 0; i < num_nodes - n - 1; i++) {
            original_head = original_head->next;
        }

        original_head->next = (original_head->next)->next;

        return answer;
    }
};
