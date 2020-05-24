/*
25. Reverse Nodes in k-Group (Hard)

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode aug(0);
        aug.next = head;
        swapK(&aug, k);
        return aug.next;
    }
    
    void swapK(ListNode* prev_head, int k) {
        ListNode *head = prev_head->next;
        ListNode *curr = prev_head;
        int k2 = k;
        while (k2 > 0 && curr != NULL) {
            curr = curr->next;
            k2--;
        }
            
        if (k2 == 0 && curr != NULL) {
            if (curr->next)
                swapK(curr, k);
            ListNode* tail=head;
            // remove tmp->next, insert after prev_head
            while(prev_head->next != curr) {
                ListNode* tmp=tail->next;
                tail->next = tmp->next;
                tmp->next = prev_head->next;
                prev_head->next = tmp;
            }
        }
    }
};