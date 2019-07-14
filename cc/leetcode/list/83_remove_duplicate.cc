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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL)
            return NULL;
        ListNode aug(0);
        aug.next = head;
        ListNode* tmp = head;
        while (tmp->next != NULL) {
            if (tmp->next->val == tmp->val) {
                tmp->next = tmp->next->next;
            } else
                tmp = tmp->next;
        }
        return aug.next;
    }
};