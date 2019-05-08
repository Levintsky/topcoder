'''
138. Copy List with Random Pointer (Medium)

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        iter_ = head
        # next_ = RandomListNode()

        # First round: make copy of each node,
        #   and link them together side-by-side in a single list.
        # 1 -> 2 -> 3
        # 1 -> 1 -> 2 -> 2 -> 3 -> 3
        while iter_ is not None:
        	next_ = iter_.next

        	copy = Node(iter_.val, next_, None)
        	iter_.next = copy

        	iter_ = next_

        # Second round: assign random pointers for the copy nodes.
        iter_ = head
        while iter_ is not None:
        	if iter_.random is not None:
        		iter_.next.random = iter_.random.next
        	iter_ = iter_.next.next

        # Third round: restore the original list, and extract the copy list.
        iter_ = head
        pseudoHead = Node(0, None, None)
        copyIter = pseudoHead

        while iter_ is not None:
            next_ = iter_.next.next

            # extract the copy
            copy = iter_.next
            copyIter.next = copy
            copyIter = copy

            # restore the original list
            iter_.next = next_

            iter_ = next_

        return pseudoHead.next

       
    def solve2(self, head):
        # make a copy with only next
        # old list: node -> id
        memo_node_id = {}
        # new list: id -> node
        memo_id_node = {}
        aux_head = Node(0, None, None)
        node = head
        new_node = aux_head
        cnt = 0

        while node is not None:
            new_node.next = Node(node.val, None, None)
            memo_node_id[node] = cnt
            memo_id_node[cnt] = new_node.next
            node = node.next
            new_node = new_node.next
            cnt += 1

        # step 2: go through the list, handle random
        n1 = head
        n2 = aux_head.next
        while n1 is not None:
        	if n1.random is not None:
                idx = memo_node_id[n1.random]
                n2.random = memo_id_node[idx]
            n1 = n1.next
            n2 = n2.next
        return aux_head.next
