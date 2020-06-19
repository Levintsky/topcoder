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
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        // step 1: traverse
        unordered_map<int, vector<int>> memo;
        
        traverse(root, memo);
        
        // step 2: bfs
        queue<int> q;
        q.push(target->val);
        unordered_set<int> s;
        while (K > 0 && q.size() > 0) {
            queue<int> q2;
            while (q.size() > 0) {
                int tmp = q.front();
                q.pop();
                s.insert(tmp);
                for (int item : memo[tmp]) {
                    if (s.find(item) == s.end())
                        q2.push(item);
                }
            }
            K--;
            swap(q, q2);
        }
        
        vector<int> result;
        while (q.size() > 0) {
            result.push_back(q.front());
            q.pop();
        }
        return result;
    }
    
    void traverse(TreeNode* node, unordered_map<int, vector<int>>& memo) {
        if (node->left != nullptr) {
            memo[node->val].push_back(node->left->val);
            memo[node->left->val].push_back(node->val);
            traverse(node->left, memo);
        }
        
        if (node->right != nullptr) {
            memo[node->val].push_back(node->right->val);
            memo[node->right->val].push_back(node->val);
            traverse(node->right, memo);
        }
    }
};
