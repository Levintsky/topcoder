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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* tmpA = headA;
        ListNode* tmpB = headB;
        
        while (tmpA != tmpB) {
            if (tmpA != NULL)
                tmpA = tmpA->next;
            else
                tmpA = headB;
            if (tmpB != NULL)
                tmpB = tmpB->next;
            else
                tmpB = headA;
        }
        return tmpA;
    }
};