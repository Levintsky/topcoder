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
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        int n = pre.size();
        if (n == 0)
            return NULL;
        return helper(pre, post, 0, n-1, 0, n-1);
    }
    
    TreeNode* helper(vector<int>& pre, vector<int>& post, int i1, int j1, int i2, int j2) {
        if (i1 > j1)
            return NULL;
        TreeNode* root = new TreeNode(pre[i1]);
        if (i1 == j1)
            return root;
        i1++;
        j2--;
        int offset = 1;
        unordered_set<int> memo1({pre[i1]}), memo2({post[i2]});
        while (memo1 != memo2) {
            memo1.insert(pre[i1+offset]);
            memo2.insert(post[i2+offset]);
            offset++;
        }
        TreeNode* left = helper(pre, post, i1, i1+offset-1, i2, i2+offset-1);
        TreeNode* right = helper(pre, post, i1+offset, j1, i2+offset, j2);
        root->left = left;
        root->right = right;
        return root;
    }
};

// Solution 2: faster!
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
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        int n = pre.size();
        if (n == 0)
            return NULL;
        return helper(pre, post, 0, n-1, 0, n-1);
    }
    
    TreeNode* helper(vector<int>& pre, vector<int>& post, int i1, int j1, int i2, int j2) {
        if (i1 > j1)
            return NULL;
        TreeNode* root = new TreeNode(pre[i1]);
        if (i1 == j1)
            return root;
        i1++;
        j2--;
        int offset = 0;
        while (pre[i1] != post[i2+offset])
            offset++;
        TreeNode* left = helper(pre, post, i1, i1+offset, i2, i2+offset);
        TreeNode* right = helper(pre, post, i1+offset+1, j1, i2+offset+1, j2);
        root->left = left;
        root->right = right;
        return root;
    }
};
