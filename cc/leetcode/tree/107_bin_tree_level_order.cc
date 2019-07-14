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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        queue<TreeNode*> q1;
        queue<TreeNode*> q2;
        
        vector<vector<int>> res;
        if (root == NULL)
            return res;
        q1.push(root);
        while (!q1.empty()) {
            vector<int> arr;
            while (!q1.empty()) {
                auto tmp = q1.front();
                arr.push_back(tmp->val);
                if (tmp->left)
                    q2.push(tmp->left);
                if (tmp->right)
                    q2.push(tmp->right);
                q1.pop();
            }
            res.push_back(arr);
            swap(q1, q2);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};