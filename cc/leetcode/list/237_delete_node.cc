/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        if (!node)
            return;
            
        ListNode* tmp = node->next;
        while (tmp->next) {
            node->val = tmp->val;
            node = tmp;
            tmp = tmp->next;
        }
        node->val = tmp->val;
        node->next = NULL;
    }
};

// better! smart!
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val =  node->next->val;
        node->next = node->next->next;
    }
};