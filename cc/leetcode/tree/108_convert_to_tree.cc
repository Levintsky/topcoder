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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        TreeNode* head = helper(nums, 0, nums.size()-1);
        return head;
    }
    TreeNode* helper(vector<int>& nums, int i, int j) {
        if (i > j)
            return NULL;
        if (i == j) {
            TreeNode* tmp = new TreeNode(nums[i]);
            return tmp;
        } else {
            int mid = (i + j + 1) / 2;
            TreeNode* tmp = new TreeNode(nums[mid]);
            tmp->left = helper(nums, i, mid-1);
            tmp->right = helper(nums, mid+1, j);
            return tmp;
        }
    }
};