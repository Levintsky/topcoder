"""
1022. Sum of Root To Leaf Binary Numbers (Easy)

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.



Example 1:

Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cnt = 0
        self.helper(0, root)
        return self.cnt

        def helper(prefix, node):
            if node is None:
                return 0
            # update prefix
            prefix = (prefix * 2 + node.val) % (10 ** 9 + 7)
            if node.left is None and node.right is None:
                self.cnt = (self.cnt + prefix) % (10 ** 9 + 7)
            if node.left is not None:
                helper(prefix, node.left)
            if node.right is not None:
                helper(prefix, node.right)
