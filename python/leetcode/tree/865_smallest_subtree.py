"""
865. Smallest Subtree with all the Deepest Nodes (Medium)

Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree. 

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:

We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
 

Note:

The number of nodes in the tree will be between 1 and 500.
The values of each node are unique.
"""

import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        memo = {root: None} # node to parent
        # 1. level-order traversal
        q = collections.deque()
        q.append(root)
        last = []
        while q:
            q2 = collections.deque()
            last = []
            while q:
                n = q.popleft()
                last.append(n)
                if n.left:
                    q2.append(n.left)
                    memo[n.left] = n
                if n.right:
                    q2.append(n.right)
                    memo[n.right] = n
            q = q2
        # 2. find lca
        tmp_set = set(last)
        while len(tmp_set) > 1:
            new_set = set()
            for n in tmp_set:
                new_set.add(memo[n])
            tmp_set = new_set
        item = tmp_set.pop()
        return item


if __name__ == "__main__":
    a = Solution()
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n3.left, n3.right = n5, n1
    n5.left, n5.right = n6, n2
    n2.left, n2.right = n7, n4
    n1.left, n1.right = n0, n8
    n = a.subtreeWithAllDeepest(n3)
    print(n.val)
