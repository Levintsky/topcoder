"""
234. Palindrome Linked List (Easy)

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

"""
1. fast, slow head to find middle node;
2. reverse the second half;
3. check;
4. reverse back;

check: https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        while head is not None:
            result.append(head.val)
            result = result.next
        if result == result[::-1]:
            return True
        else:
            return False
