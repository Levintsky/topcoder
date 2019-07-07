"""
1110. Delete Nodes And Return Forest (Medium)

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.result = []
        if root is None:
            return self.result
        self.helper(root, to_delete, False)
        return self.result

    def helper(self, node, to_delete, has_root):
        if node is None:
            return
        if not has_root and node.val not in to_delete:
            self.result.append(node)

        if node.val in to_delete:
            self.helper(node.left, to_delete, False)
            self.helper(node.right, to_delete, False)
        else:
            # node is not deleted
            if node.left is not None and node.left.val in to_delete:
                # left to be deleted
                n = node.left
                node.left = None
                self.helper(n, to_delete, True)
            else:
                self.helper(node.left, to_delete, True)
            if node.right is not None and node.right.val in to_delete:
                n = node.right
                node.right = None
                self.helper(n, to_delete, True)
            else:
                self.helper(node.right, to_delete, True)

    def solve2(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root: return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root
        helper(root, True)
        return res

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    a = Solution()
    a.delNodes(n1, [3, 5])
