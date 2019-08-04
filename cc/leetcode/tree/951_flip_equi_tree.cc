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
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        // edge case
        if (root1 == NULL)
            return root2 == NULL;
        if (root2 == NULL)
            return root1 == NULL;
        if (root1->val != root2->val)
            return false;
        // left, left / right, right
        if (flipEquiv(root1->left, root2->left) && flipEquiv(root1->right, root2->right))
            return true;
        if (flipEquiv(root1->left, root2->right) && flipEquiv(root1->right, root2->left))
            return true;
        return false;
    }
};
