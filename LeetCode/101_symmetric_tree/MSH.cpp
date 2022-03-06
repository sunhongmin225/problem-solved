#include <cstddef>

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

    bool two_nodes_are_symmetric (TreeNode* left_node, TreeNode* right_node) {
        if (left_node == nullptr && right_node == nullptr) { return true; }
        else if (left_node == nullptr && right_node != nullptr) { return false; }
        else if (left_node != nullptr && right_node == nullptr) { return false; }
        else if (left_node->val != right_node->val) { return false; }

        return two_nodes_are_symmetric (left_node->left, right_node->right) && two_nodes_are_symmetric (left_node->right, right_node->left);
    }

    bool isSymmetric(TreeNode* root) {
        return two_nodes_are_symmetric (root, root);
    }
};
