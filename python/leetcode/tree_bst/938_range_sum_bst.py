"""
938. Range Sum of BST (Easy)

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.result = 0

        def traversal(node):
            if node is None:
                return
            if node.left is not None and node.val >= L:
                # if too small, no need to traverse left
                traversal(node.left)
            if node.val >= L and node.val <= R:
                self.result += node.val
            if node.right is not None and node.val <= R:
                traversal(node.right)

        traversal(root)
        return self.result
