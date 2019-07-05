"""
589. N-ary Tree Preorder Traversal (Easy)

Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

Note:

Recursive solution is trivial, could you do it iteratively?
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        
        def traverse(node):
            if node is None:
                return
            self.res.append(node.val)
            if node.children is None:
                return
            for c in node.children:
                traverse(c)
        
        traverse(root)
        return self.res

    def solve2(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            n = stack.pop()
            if n is None:
                continue
            res.append(n.val)
            if n.children is not None:
                for c in n.children[::-1]:
                    stack.append(c)
        
        return res