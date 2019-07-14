/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int sum;
    int sumOfLeftLeaves(TreeNode* root) {
        sum = 0;
        helper(root, false);
        return sum;
    }
    
    void helper(TreeNode* node, bool from_left) {
        if (!node)
            return;
        if (node->left == NULL and node->right == NULL) {
            if (from_left)
                sum += node->val;
        }
        if (node->left)
            helper(node->left, true);
        if (node->right)
            helper(node->right, false);
    }
};
