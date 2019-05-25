"""
897. Increasing Order Search Tree (Easy)

Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.last = None
        self.root = None
        def in_order(node):
            if node is None: return
            if node.left is not None: in_order(node.left)
            # visit self
            if self.last is not None:
                self.last.right = node
            else:
                self.root = node
            node.left = None
            self.last = node
            # visit right
            if node.right is not None:
                in_order(node.right)
        in_order(root)
        return self.root


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)
    n5.left, n5.right = n3, n6
    n3.left, n3.right = n2, n4
    n2.left = n1
    n6.right = n8
    n8.left, n8.right = n7, n9
    a = Solution()
    r = a.increasingBST(n5)
    while r is not None:
        print(r.val)
        assert r.left is None
        r = r.right
