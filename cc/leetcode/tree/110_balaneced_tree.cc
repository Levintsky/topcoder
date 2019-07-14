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
    bool isBalanced(TreeNode* root) {
        int d;
        bool res = helper(root, d);
        return res;
    }
    bool helper(TreeNode* root, int& depth) {
        if (root == NULL) {
            depth = 0;
            return true;
        } else {
            int depth1, depth2;
            bool res1 = helper(root->left, depth1);
            if (!res1)
                return false;
            bool res2 = helper(root->right, depth2);
            if (!res2)
                return false;
            if (depth1 >= depth2 -1 && depth2 >= depth1 - 1) {
                depth = max(depth1, depth2) + 1;
                return true;
            } else
                return false;
        }
    }
};