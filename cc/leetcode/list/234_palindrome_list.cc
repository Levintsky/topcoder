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
    bool isPalindrome(ListNode* head) {
        vector<int> arr;
        ListNode* tmp = head;
        while (tmp) {
            arr.push_back(tmp->val);
            tmp = tmp->next;
        }
        if (arr.size() == 0)
            return true;
        int i = 0, j = arr.size() - 1;
        while (i < j) {
            if (arr[i] != arr[j])
                return false;
            i++;
            j--;
        }
        return true;
    }
};