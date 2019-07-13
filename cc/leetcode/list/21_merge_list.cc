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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* head = NULL;
		ListNode* tmp = NULL;

		while (l1 != NULL or l2 != NULL) {
			if (l2 == NULL or (l1 != NULL and l1->val < l2->val)) {
				if (head == NULL)
					head = tmp = l1;
				else {
					tmp->next = l1;
					tmp = tmp->next;
				}
				l1 = l1->next;
			} else { 
				if (head == NULL)
					head = tmp = l2;
				else {
					tmp->next = l2;
					tmp = tmp->next;
				}
				l2 = l2->next;
			}
		}
		return head;
    }
};
