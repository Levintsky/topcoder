"""
1123. Lowest Common Ancestor of Deepest Leaves (Medium)

Given a rooted binary tree, find the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.
 

Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Example 2:

Input: root = [1,2,3,4]
Output: [4]
Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]
 

Constraints:

The given tree will have between 1 and 1000 nodes.
Each node of the tree will have a distinct value between 1 and 1000.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        self.depth = {}
        self.par = {}
        
        def traverse(node, d):
            if d not in self.depth:
                self.depth[d] = []
            self.depth[d].append(node)
            if node.left is not None:
                self.par[node.left] = node
                traverse(node.left, d+1)
            if node.right is not None:
                traverse(node.right, d+1)
                self.par[node.right] = node
        
        traverse(root, 0)
        max_d = max(self.depth.keys())
        res = []
        for n in self.depth[max_d]:
            tmpres = []
            while n in self.par:
                tmpres.append(n)
                n = self.par[n]
            tmpres.append(root)
            tmpres = tmpres[::-1]
            res.append(tmpres)
        min_len = min([len(item) for item in res])
        final_res = None
        for i in range(min_len):
            items = [res[j][i] for j in range(len(res))]
            if len(set(items)) == 1:
                final_res = res[0][i]
            else:
                break
        return final_res


if __name__ == "__main__":
    a = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    print(a.lcaDeepestLeaves(n1))



