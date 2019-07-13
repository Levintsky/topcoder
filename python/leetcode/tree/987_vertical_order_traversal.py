"""
987. Vertical Order Traversal of a Binary Tree (Medium)

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

Example 1:

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        memo = {}
        result = {}
        q = collections.deque()
        q.append((root, 0))
        min_, max_ = 0, 0
        while q:
            q2 = collections.deque()
            new_res = {}
            while q:
                node, k = q.popleft()
                if k not in new_res:
                    new_res[k] = []
                new_res[k].append(node.val)
                if node.left is not None:
                    q2.append((node.left, k-1))
                    min_ = min(min_, k-1)
                if node.right is not None:
                    q2.append((node.right, k+1))
                    max_ = max(max_, k+1)
            # add values back
            for k in new_res.keys():
                new_res[k].sort()
                if k not in result:
                    result[k] = []
                for item in new_res[k]:
                    result[k].append(item)
            q = q2
            print(result)
        # arrange result
        res = []
        for i in range(min_, max_+1):
            res.append(result[i])
        return res