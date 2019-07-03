"""
776. Split BST (Medium)

Given a Binary Search Tree (BST) with root node root, and a 
target value V, split the tree into two subtrees where one 
subtree has nodes that are all smaller or equal to the target 
value, while the other subtree has all nodes that are greater 
than the target value.  It's not necessarily the case that the 
tree contains a node with value V.

Additionally, most of the structure of the original tree should 
remain.  Formally, for any child C with parent P in the original 
tree, if they are both in the same subtree after the split, then 
node C should still have the parent P.

You should output the root TreeNode of both subtrees after 
splitting, in any order.

Example 1:

Input: root = [4,2,6,1,3,5,7], V = 2
Output: [[2,1],[4,3,6,null,null,5,7]]
Explanation:
Note that root, output[0], and output[1] are TreeNode objects, not arrays.

The given tree [4,2,6,1,3,5,7] is represented by the following diagram:

          4
        /   \
      2      6
     / \    / \
    1   3  5   7

while the diagrams for the outputs are:

          4
        /   \
      3      6      and    2
            / \           /
           5   7         1
Note:

The size of the BST will not exceed 50.
The BST is always valid and each node's value is different.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if root is None:
            return [None, None]
        self.prev_, self.next_ = None, None
        self.memo = {root: (None, 0)}
        def inorder(node, i):
            if node is None:
                return
            if node.left is not None:
                self.memo[node.left] = (node, i+1)
                inorder(node.left, i+1)
            if node.val <= V:
                self.prev_ = node
            else:
                if self.next_ is None or self.next_.val >= node.val:
                    self.next_ = node
            if node.right is not None:
                self.memo[node.right] = (node, i+1)
                inorder(node.right, i+1)
        inorder(root, 0)
        print(self.prev_, self.memo[self.prev_][1])
        print(self.next_, self.memo[self.next_][1])

        # case 1: all > target
        if self.prev_ is None:
            return [None, root]
        elif self.next_ is None:
            return [root, None]
        else:
            lprev = self.memo[self.prev_][1]
            lnext = self.memo[self.next_][1]
            # case 1: prev_ is left children of next_
            res1 = prev_
            if res1 is not root:
                par = self.memo_[self.prev_]
                if par.left is self.prev_:
                    par.left = self.prev_.right
                    self.prev_.right = None
                else:
                    par.right = self.prev_.right
                    self.prev_.right = None

            # case 2: next_ is right children of prev_

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n4.left, n4.right = n2, n6
    n2.left, n2.right = n1, n3
    n6.left, n6.right = n5, n7
    a = Solution()
    print(a.splitBST(n4, 2))