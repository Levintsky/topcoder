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
    bool btreeGameWinningMove(TreeNode* root, int n, int x) {
        vector<int> memo(n+1, 0);
        vector<TreeNode*> memo2(n+1, NULL);
        traverse(root, memo, memo2);
        auto tmpn = memo2[x]; // the node
        int cnt1 = 0, cnt2 = 0, cnt3 = 0;
        if (tmpn->left != NULL)
            cnt1 = memo[tmpn->left->val];
        if (tmpn->right != NULL)
            cnt2 = memo[tmpn->right->val];
        cnt3 = n - memo[x];
        return max({cnt1, cnt2, cnt3}) * 2 > n;
    }
    
    void traverse(TreeNode* node, vector<int>& memo, vector<TreeNode*>& memo2) {
        // traverse, 
        int cnt = 1;
        if (node->left != NULL) {
            traverse(node->left, memo, memo2);
            cnt += memo[node->left->val];
        }
        if (node->right != NULL) {
            traverse(node->right, memo, memo2);
            cnt += memo[node->right->val];
        }
        memo[node->val] = cnt;
        memo2[node->val] = node;
    }
};
