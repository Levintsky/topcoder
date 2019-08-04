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
    int distributeCoins(TreeNode* root) {
        auto res = helper(root);
        return res.second;
    }
    
    pair<int, int> helper(TreeNode* root) {
        if (root == NULL)
            return {0, 0};
        if (root->left == NULL && root->right == NULL) {
            int c = root->val - 1;
            return {c, abs(c)};
        }
        auto res1 = helper(root->left);
        auto res2 = helper(root->right);
        int c = res1.first + res2.first + root->val - 1;
        int m = abs(c) + res1.second + res2.second;
        return {c, m};
    }
};
