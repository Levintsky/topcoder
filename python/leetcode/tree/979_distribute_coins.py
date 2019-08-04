"""
979. Distribute Coins in Binary Tree (Medium)

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin. 

Example 1:

Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:

Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.

Example 3:

Input: [1,0,2]
Output: 2

Example 4:

Input: [1,0,0,null,3]
Output: 4

Note:

1<= N <= 100
0 <= node.val <= N
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, res = self.helper(root)
        return res
        
    def helper(self, node):
        # if extra coins, return c+, moves to move
        # if short of coints, return c-, moves to move
        if node is None:
            return 0, 0
        # edge case: leaf node
        if not node.left and not node.right:
            return node.val - 1, abs(node.val - 1)
        c1, n1 = self.helper(node.left)
        c2, n2 = self.helper(node.right)
        c = node.val + c1 + c2 - 1
        return c, abs(c) + n1 + n2


if __name__ == "__main__":
    a = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(0)
    n3 = TreeNode(0)
    n4 = TreeNode(3)
    n1.left, n1.right = n2, n3
    n2.right = n4
    print(a.distributeCoins(n1))
