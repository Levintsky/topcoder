"""
156. Binary Tree Upside Down (Medium)

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""

"""
 x
y z
become
 y
z x
but cache y's left and right before the swap,
and give them to z
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        rec = []
        node = root

        while node is not None:
            n1, n2, n3 = node, node.left, node.right
            n1.left, n1.right = None, None
            rec.append((n1, n2, n3))
            node = n2

        new_root = rec[-1][0]
        rec.pop()
        node = new_root

        while len(rec) != 0:
            n, l, r = rec.pop()
            l.left = r
            l.right = n
        return new_root

    def solve2(self, root):
        self.root = None
        self.helper(root)
        return self.root

    def helper(self, node):
        if node is None:
            return None
        if node.left is not None:
            self.helper(node.left)
            l, r = node.left, node.right
            l.left, l.right = r, node
            node.left, node.right = None, None
        else:
            self.root = node


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5

    a = Solution()
    # n = a.upsideDownBinaryTree(n1)
    n = a.solve2(n1)

    # print n.val, n.left.val, n.right.val
    # print n.right.left.val, n.right.right.val
