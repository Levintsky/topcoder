"""
742. Closest Leaf in a Binary Tree (Medium)

Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
Note:
root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # step 1: for each node, calculate closest leaf underself and distance
        self.memo = {} # node to closest leaf under (val and distance)
        self.par = {}
        def find_closest(node):
            if node is None:
                return None, None
            
            if node.left is not None:
                self.par[node.left.val] = node.val
            if node.right is not None:
                self.par[node.right.val] = node.val
                
            if node.left is None and node.right is None:
                self.memo[node.val] = (node.val, 0)
                return node.val, 0
            elif node.left is None:
                v, d = find_closest(node.right)
                self.memo[node.val] = (v, d+1)
                return v, d+1
            elif node.right is None:
                v, d = find_closest(node.left)
                self.memo[node.val] = (v, d+1)
                return v, d+1
            else: # both left and right
                v1, d1 = find_closest(node.left)
                v2, d2 = find_closest(node.right)
                if d1 <= d2:
                    self.memo[node.val] = (v1, d1+1)
                    return v1, d1+1
                else:
                    self.memo[node.val] = (v2, d2+1)
                    return v2, d2+1
        
        find_closest(root)
        print(self.memo)
        print(self.par)
        v1, d1 = self.memo[k]
        if k in self.par: # not root
            k2 = self.par[k]
            v2, d2 = self.memo[k2]
            d2 += 1
            if d2 < d1:
                return v2
        return v1


if __name__ == "__main__":
    a = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1.left, n1.right = n2, n3
    n2.left = n4
    n4.left = n5
    n5.left = n6
    print(a.findClosestLeaf(n1, 2))




