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
    int pathSum(TreeNode* root, int sum) {
        if (!root)
            return 0;
        int cnt = 0;
        if (root->left)
            cnt += pathSum(root->left, sum);
        if (root->right)
            cnt += pathSum(root->right, sum);
        cnt += helper(root, sum);
        return cnt;
    }
    
    int helper(TreeNode* root, int sum) {
        if (!root)
            return 0;
        int cnt = 0;
        if (root->val == sum)
            cnt++;
        // include root
        if (root->left)
            cnt += helper(root->left, sum - root->val);
        if (root->right)
            cnt += helper(root->right, sum - root->val);
        return cnt;
    }
};
