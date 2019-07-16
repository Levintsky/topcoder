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
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        if (root == NULL)
            return NULL;
        unordered_map<TreeNode*, TreeNode*> memo;
        queue<TreeNode*> q1;
        vector<TreeNode*> last;
        q1.push(root);
        while (q1.size() > 0) {
            last.clear();
            queue<TreeNode*> q2;
            while (q1.size() > 0) {
                auto n = q1.front();
                last.push_back(n);
                q1.pop();
                if (n->left != NULL) {
                    q2.push(n->left);
                    memo[n->left] = n;
                }
                if (n->right != NULL) {
                    q2.push(n->right);
                    memo[n->right] = n;
                }
            }
            swap(q1, q2);
        }
        // lca
        unordered_set<TreeNode*> s1;
        for (auto item : last)
            s1.insert(item);
        while (s1.size() > 1) {
            unordered_set<TreeNode*> s2;
            for (auto item : s1)
                s2.insert(memo[item]);
            s1.clear();
            swap(s1, s2);
        }
        // return the only item
        TreeNode* res = NULL;
        for (auto item : s1)
            res = item;
        return res;
    }
};

// recursive approach: better!
class Solution {
public:
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        return deep(root).second;
    }
    
    pair<int, TreeNode*> deep(TreeNode* root) {
        if (!root)
            return {0, NULL};
        pair<int, TreeNode*> l = deep(root->left), r = deep(root->right);
        
        int d1 = l.first, d2 = r.first;
        if (d1 == d2)
            return {d1+1, root};
        else if (d1 > d2)
            return {d1+1, l.second};
        else
            return {d2+1, r.second};
    }
};
