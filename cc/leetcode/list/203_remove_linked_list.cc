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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode aug(0);
        aug.next = head;
        ListNode* tmp = &aug;
        while (tmp->next != NULL) {
            if (tmp->next->val == val) {
                // auto tmp2 = tmp->next;
                tmp->next = tmp->next->next;
                // delete tmp2;
            } else
                tmp = tmp->next;
        }
        return aug.next;
    }
};