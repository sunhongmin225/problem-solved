// Reference: https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/106645/C%2B%2BJava-*-BFSDFS3liner-Clean-Code-With-Explanation
// Need to get used to preorder (or in- or post-) traversal
#include <vector>
#include <cstddef>
#include <algorithm>
#include <initializer_list>

using namespace std;
class Solution {
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

public:
    unsigned int dfs (TreeNode* node, unsigned int idx, int depth, vector<int>& lefts) {
        if (node == nullptr) { return 0; }
        if (depth >= lefts.size()) { lefts.push_back(idx); }
        unsigned int left_val  = dfs(node->left , idx * 2 + 1, depth + 1, lefts);
        unsigned int right_val = dfs(node->right, idx * 2 + 2, depth + 1, lefts);
        return max({idx + 1 - lefts[depth], left_val, right_val});
    }

    int widthOfBinaryTree (TreeNode* root) {
        vector<int> lefts;
        return (int) dfs(root, 0, 0, lefts);
    }
};
