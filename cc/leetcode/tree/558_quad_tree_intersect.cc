/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() {}

    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/
class Solution {
public:
    Node* intersect(Node* q1, Node* q2) {
        if (!q1) return q2;
        if (!q2) return q1;
        if (q1->isLeaf) {
            if (q1->val)
                return q1;
            else
                return q2;
        }
        if (q2->isLeaf){
            if (q2->val)
                return q2;
            else
                return q1;
        }
        auto t1 = intersect(q1->topLeft, q2->topLeft);
        auto t2 = intersect(q1->topRight, q2->topRight);
        auto t3 = intersect(q1->bottomLeft, q2->bottomLeft);
        auto t4 = intersect(q1->bottomRight, q2->bottomRight);
        if (t1->isLeaf && t2->isLeaf && t3->isLeaf && t4->isLeaf && t1->val == t2->val &&t2->val == t3->val && t3->val == t4->val)
            return new Node(t1->val, true, NULL, NULL, NULL, NULL);
        return new Node(false, false, t1, t2, t3, t4);
    }
};
