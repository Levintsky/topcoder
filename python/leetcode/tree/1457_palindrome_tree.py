"""
1457. Pseudo-Palindromic Paths in a Binary Tree (Medium)

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:

Input: root = [9]
Output: 1
 

Constraints:

The given binary tree will have between 1 and 10^5 nodes.
Node values are digits from 1 to 9.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.helper(root, [])
        return self.result
        
    def helper(self, node, curr_list):
        if node is None:
            self.result += 1
            return
        
        curr_list.append(node.val)
        
        if node.left is None and node.right is None:
            cnt = [0] * 9
            for item in curr_list:
                cnt[item-1] += 1
            cnt = [item % 2 for item in cnt]
            if sum(cnt) <= 1:
                self.result += 1
        
        if node.left is not None:
            self.helper(node.left, curr_list)
        if node.right is not None:
            self.helper(node.right, curr_list)
        curr_list.pop()
        return
        