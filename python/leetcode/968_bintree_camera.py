"""
968. Binary Tree Cameras (Hard)

Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:

Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:
Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all 
nodes of the tree. The above image shows one of the valid 
configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""

"""
Idea 1: (bottom-up)
all leaves's parent as camera, then remove
  memo1: node -> parent
iterate:
  remove leaves;
  add their parent as camera;
  remove parent(camera)'s parent

Idea 2: (top-down)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.memo = {}

    def solve2(self, root):
        def helper(node):
            # given a node,
            # return min if only the root node is unattended
            # return min if everything is attended
            # return min if everything and the node is attended
            if node is None:
                return 0, 0, 0
            if node.left is None and node.right is None:
                return 0, 1, 1
            if node.left is None:
                min_l1, min_l2 = helper(node.right)
                return (min(min_l1, min_l2),)
