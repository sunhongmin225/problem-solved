/*
1. Try to reduce edge cases by generalizing the solution
2. Divide-and-conquer
*/
#include <cstddef>
#include <cmath>

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

    // find parent of target (key)
    TreeNode* find_parent (TreeNode* root, int key, TreeNode* parent) {
        if (root->val == key) {
            return parent;
        } else if (root->val > key) {
            if (root->left == nullptr) { return nullptr; }
            else { return find_parent (root->left, key, root); }
        } else { // root->val < key
            if (root->right == nullptr) { return nullptr; }
            else { return find_parent (root->right, key, root); }
        }
    }

    TreeNode* find_parent_of_leftmost_child (TreeNode* target, TreeNode* parent) {
        if (target->left == nullptr) { return parent; }
        else return find_parent_of_leftmost_child (target->left, target);
    }

    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == nullptr) { return root; } // edge case
        TreeNode dummy_node = TreeNode(pow(10, 5) + 1); // impossible value assigned
        TreeNode* parent = find_parent (root, key, &dummy_node);
        if (parent == nullptr) { // key not found
            return root;
        }

        TreeNode* target;
        bool is_left = false;
        if (parent == &dummy_node) { // root value is key itself
            target = root;
        } else {
            if (parent->left != nullptr && parent->left->val == key) { is_left = true; target = parent->left; }
            else if (parent->right != nullptr && parent->right->val == key) { target = parent->right; }
        }

        // Case 1: target is leaf
        if (target->left == nullptr && target->right == nullptr) {
            if (parent == &dummy_node) { return nullptr; }
            else {
                if (is_left) { parent->left = nullptr; }
                else { parent->right = nullptr; }
            }

        // Case 2-1: target only has right child
        } else if (target->left == nullptr && target->right != nullptr) {
            target->val = target->right->val;
            target->left = target->right->left; // target->left must be modified first
            target->right = target->right->right;

        // Case 2-2: target only has left child
        } else if (target->left != nullptr && target->right == nullptr) {
            target->val = target->left->val;
            target->right = target->left->right; //target->right must be modified first
            target->left = target->left->left;

        // Case 3: target has both children
        } else if (target->left != nullptr && target->right != nullptr) {
            TreeNode* parent_of_leftmost_child = find_parent_of_leftmost_child(target->right, &dummy_node);
            if (parent_of_leftmost_child == &dummy_node) { // target->right itself is the leftmost child
                target->val = target->right->val;
                target->right = target->right->right;
            } else {
                target->val = parent_of_leftmost_child->left->val;
                parent_of_leftmost_child->left = parent_of_leftmost_child->left->right;
            }
        }

        return root;
    }
};
