// 1. First attempt: Tried to directly find parents by using the position of TreeNode *p, and TreeNode *q, but failed since it wasn't a balanced binary tree
// 2. Second attempt: Backtracking using stack
// 3. But still unsatisfactory when finding common ancestors between two stacks, since I've introduced two additional vector<TreeNode *> variables and searched for each vector multiple times)

#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    };

    TreeNode* find_by_val (stack<TreeNode *> &ancestors, TreeNode *node, int target_val) {
        ancestors.push(node);
        if (node->val == target_val) { return node; }
        if (node->left != NULL) {
            TreeNode* ans = find_by_val(ancestors, node->left, target_val);
            if (ans != NULL) { return ans; }
        }
        if (node->right != NULL) {
            TreeNode* ans = find_by_val(ancestors, node->right, target_val);
            if (ans != NULL) { return ans; }
        }
        ancestors.pop(); // backtrack when leaf node is encountered
        return NULL; // NULL is an indicator for failed search
    }

    // returns true if list contains node, o.w. returns false
    bool contains (vector<TreeNode *> &list, TreeNode *node) {
        for (int i = 0; i < list.size(); i++) {
            if (list[i]->val == node->val) { return true; }
        }
        return false;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        stack<TreeNode *> p_ancestors;
        stack<TreeNode *> q_ancestors;
        find_by_val(p_ancestors, root, p->val);
        find_by_val(q_ancestors, root, q->val);

        // convert stack<TreeNode *> to vector<TreeNode *> for convenience
        vector<TreeNode *> p_ancestors_list;
        vector<TreeNode *> q_ancestors_list;
        while(!p_ancestors.empty()) {
            TreeNode* node = p_ancestors.top();
            p_ancestors_list.push_back(node);
            p_ancestors.pop();
        }
        while(!q_ancestors.empty()) {
            TreeNode* node = q_ancestors.top();
            q_ancestors_list.push_back(node);
            q_ancestors.pop();
        }

        // find least common ancestors between two lists
        if (p_ancestors_list.size() > q_ancestors_list.size()) {
            for (int i = 0; i < q_ancestors_list.size(); i++) {
                if (contains(p_ancestors_list, q_ancestors_list[i])) {
                    return q_ancestors_list[i];
                }
            }
        } else {
            for (int i = 0; i < p_ancestors_list.size(); i++) {
                if (contains(q_ancestors_list, p_ancestors_list[i])) {
                    return p_ancestors_list[i];
                }
            }
        }
        return root; // should not reach here
    }
};
