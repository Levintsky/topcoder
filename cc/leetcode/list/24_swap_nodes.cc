/*
24. Swap Nodes in Pairs (Medium)

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
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
    ListNode* swapPairs(ListNode* head) {
        ListNode aug(0);
        aug.next = head;
        ListNode *n = &aug;
        while (n != NULL) {
            ListNode *n1 = n->next;
            if (n1 == NULL)
                break;
            ListNode *n2 = n1->next;
            if (n2 == NULL)
                break;
            ListNode *n3 = n2->next;
            n->next = n2;
            n2->next = n1;
            n1->next = n3;
            n = n1;
        }
        return aug.next;
    }
};
