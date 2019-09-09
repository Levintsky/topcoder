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
    ListNode* removeZeroSumSublists(ListNode* head) {
        if (head == NULL)
            return head;
        ListNode aux(0);
        aux.next = head;
        unordered_map<int, ListNode*> memo;
        memo[0] = &aux;
        ListNode* n = head;
        int curr = 0;
        while (n != NULL) {
            curr += n->val;
            if (memo.find(curr) == memo.end()) {
                memo[curr] = n;
                n = n->next;
            } else {
                ListNode* target_node=memo[curr];
                ListNode* target_next=n->next;
                int tmpv = curr;
                while (target_node->next != target_next) {
                    tmpv += target_node->next->val;
                    if (tmpv != curr)
                        memo.erase(tmpv);
                    target_node->next = target_node->next->next;
                }
                target_node->next = target_next;
                n = target_next;
            }
        }
        return aux.next;
    }
};
