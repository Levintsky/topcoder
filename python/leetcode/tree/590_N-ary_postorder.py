"""
590. N-ary Tree Postorder Traversal (Easy)

Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].

 
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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        
        def traverse(node):
            if node is None:
                return
            if node.children is not None:
                for c in node.children:
                    traverse(c)
            res.append(node.val)
        
        traverse(root)
        return res

    def solve2(self, root):
        res = []
        
        stack = [[root, False]]
        while stack:
            # get last
            if stack[-1][0] is None:
                _ = stack.pop()
            elif stack[-1][1]:
                n, _ = stack.pop()
                res.append(n.val)
            else:
                stack[-1][1] = True
                n = stack[-1][0]
                if n.children is not None:
                    for c in n.children[::-1]:
                        stack.append([c, False])
        return res

    def solve3(self, root):
    	if not root:
            return []
        
        stack, output = [root], []
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                for c in root.children:
                    stack.append(c)
        return output[::-1]