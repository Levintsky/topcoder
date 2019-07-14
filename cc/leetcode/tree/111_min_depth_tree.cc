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
    int minDepth(TreeNode* root) {
        if (root == NULL)
            return 0;
        int res1 = minDepth(root->left);
        int res2 = minDepth(root->right);
        if (res1 == 0 && res2 == 0)
            return 1;
        else if (res1 > 0 && res2 > 0)
            return 1 + min(res1, res2);
        else if (res1 == 0)
            return 1 + res2;
        else
            return 1 + res1;
    }
};