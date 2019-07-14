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
    ListNode* reverseList(ListNode* head) {
        auto tmp = head;
        if (!head)
            return NULL;
        ListNode aug(0);
        aug.next = head;
        while (tmp->next) {
            auto n = tmp->next;
            tmp->next = n->next;
            n->next = aug.next;
            aug.next = n;
        }
        return aug.next;
    }
};