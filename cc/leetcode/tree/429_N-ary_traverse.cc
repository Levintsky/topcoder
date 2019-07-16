/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        queue<Node*> q1;
        queue<Node*> q2;
        q1.push(root);
        vector<vector<int>> res;
        if (!root)
            return res;
        
        while (q1.size() > 0) {
            vector<int> tmpres;
            while (q1.size() > 0) {
                auto n = q1.front();
                for (auto item : n->children)
                    q2.push(item);
                tmpres.push_back(n->val);
                q1.pop();
            }
            res.push_back(tmpres);
            swap(q1, q2);
        }
        return res;
    }

};
