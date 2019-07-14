/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// Solution 1: naive
class Solution {
public:
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root)
            return NULL;
        unordered_map<TreeNode*, TreeNode*> par;
        helper(root, par);
        vector<TreeNode*> arr_p(1, p);
        vector<TreeNode*> arr_q(1, q);
        while (par.find(p) != par.end()) {
            p = par[p];
            arr_p.push_back(p);
        }
        while (par.find(q) != par.end()) {
            q = par[q];
            arr_q.push_back(q);
        }
        reverse(arr_p.begin(), arr_p.end());
        reverse(arr_q.begin(), arr_q.end());
        TreeNode* res;
        for (int i = 0; i < arr_p.size() && i < arr_q.size(); ++i) {
            if (arr_p[i] == arr_q[i])
                res = arr_p[i];
        }
        return res;
    }
    void helper(TreeNode* node, unordered_map<TreeNode*, TreeNode*>& par) {
        if (node == NULL)
            return;
        if (node->left != NULL) {
            par[node->left] = node;
            helper(node->left, par);
        }
        if (node->right != NULL) {
            par[node->right] = node;
            helper(node->right, par);
        }
    }
};

// better solution: BST
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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p->val == q->val)
            return p;
        if (p->val > q->val)
            swap(p, q);
        if (root->val == p->val)
            return p;
        if (root->val == q->val)
            return q;
        if (p->val < root->val && q->val < root->val)
            return lowestCommonAncestor(root->left, p, q);
        else if (p->val < root->val && q->val > root->val)
            return root;
        else
            return lowestCommonAncestor(root->right, p, q);
    }

};