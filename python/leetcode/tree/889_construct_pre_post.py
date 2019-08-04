"""
889. Construct Binary Tree from Preorder and Postorder Traversal (Medium)

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        n = len(pre)
        return self.helper(pre, post, 0, n-1, 0, n-1)
        
    def helper(self, pre, post, i1, j1, i2, j2):
        if i1 > j1:
            return None
        root = TreeNode(pre[i1])
        if j1 == i1:
            return root
        i1 += 1
        set1, set2 = set([pre[i1]]), set([post[i2]])
        offset = 1
        while set1 != set2:
            set1.add(pre[i1+offset])
            set2.add(post[i2+offset])
            offset += 1
        root.left = self.helper(pre, post, i1, i1+offset-1, i2, i2+offset-1)
        root.right = self.helper(pre, post, i1+offset, j1, i2+offset, j2-1)
        return root
        
