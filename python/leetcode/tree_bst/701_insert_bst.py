"""
701. Insert into a Binary Search Tree (Medium)

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = TreeNode(val)
        if root is None:
            return node

        # divide and conquer
        def is_leaf(n):
            return n.left is None and n.right is None

        curr = root
        while not is_leaf(curr):
            if val > curr.val and curr.right is not None:
                curr = curr.right
            elif val < curr.val and curr.left is not None:
                curr = curr.left
            else:
                break
        if curr.val > val:
            curr.left = node
        else:
            curr.right = node
        return root
