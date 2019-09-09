"""
1171. Remove Zero Sum Consecutive Nodes from Linked List (Medium)

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        aux = ListNode(0)
        aux.next = head
        memo = {0: aux} # cumsum to node
        n, curr = head, 0
        while n != None:
            curr += n.val
            if curr not in memo:
                memo[curr] = n
                n = n.next
            else: # remove last nodes until
                target_node = memo[curr]
                target_next = n.next
                # remove all nodes from [target_node.next, n]
                tmpv = curr
                while target_node.next != target_next:
                    tmpv += target_node.next.val
                    if tmpv != curr:
                        del memo[tmpv]
                    target_node.next = target_node.next.next
                target_node.next = target_next
                n = target_node.next
        return aux.next

    # better solution
    def removeZeroSumSublists(self, head):
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next
                    
                
if __name__ == "__main__":
    a = Solution()
    n = []
    arr = [1, 3, 2, -3, -2, 5, 100, -100, 1]
    for item in arr:
        n.append(ListNode(item))
    for i in range(0, len(n)-1):
        n[i].next = n[i+1]
    res = a.removeZeroSumSublists(n[0])
    print(res.val)
