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
    vector<string> result;
    vector<string> binaryTreePaths(TreeNode* root) {
        if (!root)
            return result;
        helper(root, "");
        return result;
    }
    void helper(TreeNode* node, string s) {
        if (s.size() > 0)
            s += "->";
        s += to_string(node->val);
        if (!node->left && !node->right)
            result.push_back(s);
        if (node->left)
            helper(node->left, s);
        if (node->right)
            helper(node->right, s);
    }
};