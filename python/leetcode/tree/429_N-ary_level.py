"""
429. N-ary Tree Level Order Traversal (Easy)

Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
 

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        q1 = collections.deque()
        q1.append(root)
        if root is None: return []
        
        while q1:
            q2 = collections.deque()
            subres = []
            while q1:
                n = q1.popleft()
                if n is None:
                    continue
                subres.append(n.val)
                if n.children is not None:
                    for c in n.children:
                        q2.append(c)
            q1 = q2
            res.append(subres)
        return res