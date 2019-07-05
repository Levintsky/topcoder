"""
430. Flatten a Multilevel Doubly Linked List (Medium)

You are given a doubly linked list which in addition to the next and previous 
pointers, it could have a child pointer, which may or may not point to a separate 
doubly linked list. These child lists may have one or more children of their own, 
and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. 
You are given the head of the first level of the list.

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
 

Explanation for the above example:

Given the following multilevel doubly linked list:

We should return the following flattened doubly linked list:

"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.res = []
        h, t = self.helper(head)
        return h
        
    def helper(self, node):
        # return head, tail
        if node is None:
            return None, None
        n = node
        tail = None
        # get to child
        while n is not None: # and n.child is None:
            if n.child is not None:
                h, t = self.helper(n.child)
                nnext = n.next
                n.next, n.child = h, None # fix n
                h.prev = n # fix h
                t.next = nnext # fix t
                if nnext is not None:
                    nnext.prev = t
            if n.next is None:
                tail = n
            n = n.next
        return node, tail


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n7 = Node(7)
    n8 = Node(8)
    n1.next = n2
    n2.prev, n2.next = n1, n3
    n3.prev, n3.child = n2, n7
    n7.next = n8
    n8.prev = n7

    a = Solution()
    print(a.flatten(n1))