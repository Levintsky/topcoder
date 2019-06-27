"""
1026. Maximum Difference Between Node and Ancestor (Medium)

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Example 1:

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 
Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        best, min_, max_ = self.helper(root)
        return best

    def helper(self, root):
        # corner case
        best, min_, max_ = 0, root.val, root.val
        b1, min1, max1 = None, None, None
        b2, min2, max2 = None, None, None
        if root.left is None and root.right is None:
            return 0, root.val, root.val
        if root.left is not None:
            b1, min1, max1 = self.helper(root.left)
            best = max(b1, max(max_, max1) - min(min_, min1))
            # min_ = min(min1, min_)
            # max_ = max(max1, max_)
        if root.right is not None:
            b2, min2, max2 = self.helper(root.right)
            best = max(b2, max(max_, max2) - min(min_, min2))

        if b1 is not None:
            min_, max_ = min(min_, min1), max(max_, max1)
        if b2 is not None:
            min_, max_ = min(min_, min2), max(max_, max2)

        return best, min_, max_
