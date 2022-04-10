/*
1. Remember pre- in- post-order traversals (their implementations are simple)
2. Spent quite a lot of time implementing copy_tree function
3. Let's get used to constructors (i.e., initializers) in struct
*/
#include <vector>

using namespace std;

class Solution {
public:
    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {}
        TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    };

    // new struct that is similar to TreeNode but has vector<size_t> sums in addition
    struct BiggerNode {
        int val;
        BiggerNode *left;
        BiggerNode *right;
        vector<size_t> sums; // BiggerNode created to hold sums for each node
        BiggerNode() : val(0), left(nullptr), right(nullptr) {}
        BiggerNode(int x) : val(x), left(nullptr), right(nullptr) {}
        BiggerNode(int x, BiggerNode *left, BiggerNode *right) : val(x), left(left), right(right) {}
    };

    static bool is_leaf (BiggerNode* node) {
        if (node->left == nullptr && node->right == nullptr) { return true; }
        else return false;
    }

    // need to scan from leaf nodes to the root node (children to parent)
    static void post_order_traversal (BiggerNode* node, int targetSum, int& ans) {
        if (node == nullptr)
            return;

        post_order_traversal(node->left, targetSum, ans);

        post_order_traversal(node->right, targetSum, ans);

        vector<size_t> sums;
        if (is_leaf(node)) {
            sums.push_back(node->val);
            if (node->val == targetSum) { ans++; }
        } else if (node->left == nullptr) {
            sums.push_back(node->val);
            if (node->val == targetSum) { ans++; }
            vector<size_t> r_sums = node->right->sums;
            for (int i = 0; i < r_sums.size(); i++) {
                sums.push_back(node->val + r_sums[i]);
                if (node->val + r_sums[i] == targetSum) { ans++; }
            }
        } else if (node->right == nullptr) {
            sums.push_back(node->val);
            if (node->val == targetSum) { ans++; }
            vector<size_t> l_sums = node->left->sums;
            for (int i = 0; i < l_sums.size(); i++) {
                sums.push_back(node->val + l_sums[i]);
                if (node->val + l_sums[i] == targetSum) { ans++; }
            }
        } else {
            sums.push_back(node->val);
            if (node->val == targetSum) { ans++; }
            vector<size_t> r_sums = node->right->sums;
            for (int i = 0; i < r_sums.size(); i++) {
                sums.push_back(node->val + r_sums[i]);
                if (node->val + r_sums[i] == targetSum) { ans++; }
            }
            vector<size_t> l_sums = node->left->sums;
            for (int i = 0; i < l_sums.size(); i++) {
                sums.push_back(node->val + l_sums[i]);
                if (node->val + l_sums[i] == targetSum) { ans++; }
            }
        }
        node->sums = sums;
    }

    // simply copy TreeNode* orig to BiggerNode* target
    static void copy_tree (TreeNode* orig, BiggerNode* target) {
        if (orig == nullptr) { target = nullptr; return; }
        if (orig->left != nullptr) {
            BiggerNode* b_left = new BiggerNode();
            target->val = orig->val;
            target->left = b_left;
            copy_tree (orig->left, b_left);
        }
        if (orig->right != nullptr) {
            BiggerNode* b_right = new BiggerNode();
            target->val = orig->val;
            target->right = b_right;
            copy_tree (orig->right, b_right);
        }
        // target is leaf node, so just copy the value
        target->val = orig->val;
    }

    int pathSum (TreeNode* root, int targetSum) {
        if (root == nullptr) { return 0; }
        BiggerNode* b_root = new BiggerNode();
        copy_tree (root, b_root);
        int ans = 0;
        post_order_traversal(b_root, targetSum, ans);
        return ans;
    }
};
