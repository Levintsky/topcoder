/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int result = 0;
    
    int pseudoPalindromicPaths (TreeNode* root) {
        vector<int> arr(10);
        helper(root, arr);
        return result;
    }
    
    void helper(TreeNode* node, vector<int>& arr) {
        if (node == NULL)
            return;
        arr[node->val]++;
        if (node->left == NULL && node->right == NULL){
            int odd = 0;
            for (int item : arr) {
                if (item % 2 == 1)
                    odd++;
            }
            if (odd < 2)
                result++;
        }
        if (node->left != NULL)
            helper(node->left, arr);
        if (node->right != NULL)
            helper(node->right, arr);
        arr[node->val]--;
    }
};
