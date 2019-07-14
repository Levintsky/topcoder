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
    bool isSymmetric(TreeNode* root) {
        if (root == NULL)
            return true;
        else
            return helper(root->left, root->right);
    }
    
    bool helper(TreeNode* l, TreeNode* r) {
        if (l == NULL && r == NULL)
            return true;
        else if (l == NULL || r == NULL)
            return false;
        if (l->val != r->val)
            return false;
        return helper(l->left, r->right) && helper(l->right, r->left);
        
    }
};