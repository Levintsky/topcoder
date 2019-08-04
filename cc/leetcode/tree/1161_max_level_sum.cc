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
    int maxLevelSum(TreeNode* root) {
        queue<TreeNode*> q1, q2;
        int resl = 1, resv = root->val, curr = 2;
        q1.push(root);
        while (q1.size() > 0) {
            int tmp = 0;
            while (q1.size() > 0) {
                TreeNode* tmpn = q1.front();
                q1.pop();
                if (tmpn->left != NULL) {
                    q2.push(tmpn->left);
                    tmp += tmpn->left->val;
                }
                if (tmpn->right != NULL) {
                    q2.push(tmpn->right);
                    tmp += tmpn->right->val;
                }
            }
            if (q2.size() > 0 && tmp > resv) {
                resl = curr;
                resv = tmp;
            }
            swap(q1, q2);
            curr++;
        }
        return resl;
    }
};
