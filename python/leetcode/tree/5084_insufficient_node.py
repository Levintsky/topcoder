"""
5084. Insufficient Nodes in Root to Leaf Paths (Medium)

Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.  (A leaf is a node with no children.)

A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.

Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.

Example 1:

Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]

Example 2:

Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]

Note:

The given tree will have between 1 and 5000 nodes.
-10^5 <= node.val <= 10^5
-10^9 <= limit <= 10^9
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        self.memo = {} # node to parent
        self.memo[root] = None
        self.root_flag = True
        if self.traverse(root, limit):
            return root
        else:
            return None
    
    """
    def del_node(self, node):
        par = self.memo[node]
        if par is None: # root is bad
            self.root_flag = False
        elif par.left is node:
            par.left = None
        else:
            par.right = None
    """
        
    def traverse(self, node, limit, pre):
        # edge case: empty
        if node is None:
            return
        # edge case: leaf
        if node.left is None and node.right is None:
            if node.val < limit:
                self.del_node(node)
                return False
            else:
                return True
        else: # non-leaf node
            result = []
            if node.left is not None:
                self.memo[node.left] = node
                result.append(self.traverse(node.left, limit-node.val))
            if node.right is not None:
                self.memo[node.right] = node
                result.append(self.traverse(node.right, limit-node.val))
            if True not in result:
                # delete node return False
                self.del_node(node)
                return False
            else:
                return True

    def solve2(self, root, limit):
        def dfs(root, limit, pre):
            if not root: return pre
            l = dfs(root.left, limit, pre + root.val)
            r = dfs(root.right, limit, pre + root.val)
            if root.left and l < limit: root.left = None
            if root.right and r < limit: root.right = None
            return max(l, r)
        if dfs(root, limit, 0) < limit: root = None
        return root