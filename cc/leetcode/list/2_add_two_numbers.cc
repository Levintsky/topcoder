#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* root = NULL;
        ListNode* last = NULL;
        bool carry = false;

        while (l1 != NULL or l2 != NULL) {
            ListNode* node = new ListNode(0);
            if (l1 != NULL) {
                node->val += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL) {
                node->val += l2->val;
                l2 = l2->next;
            }
            if (carry) node->val += 1;

            if (node->val >= 10) {
                node->val -= 10;
                carry = true;
            }
            else
                carry = false;
            if (root == NULL) root = node;
            
            if (last != NULL) last->next = node;
            last = node;
            
        }
        if (carry) {
            ListNode* node = new ListNode(1);
            last->next = node;
        }
        return root;
    }
};

int main() {
    ListNode* n1 = new ListNode(0);
    ListNode* n2 = new ListNode(0);
    Solution a;
    ListNode* n3 = a.addTwoNumbers(n1, n2);
}
