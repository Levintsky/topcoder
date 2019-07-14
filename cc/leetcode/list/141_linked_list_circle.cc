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
    bool hasCycle(ListNode *head) {
        if (head == NULL)
            return false;
        ListNode* slow = head->next;
        if (!slow || !slow->next)
            return false;
        ListNode* fast = slow->next;
        while (slow != fast) {
            if (fast->next && fast->next->next)
                fast = fast->next->next;
            else
                return false;
            slow = slow->next;
        }
        return true;
    }
};