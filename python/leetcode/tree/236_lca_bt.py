"""
236. Lowest Common Ancestor of a Binary Tree (Medium)

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""

"""
Same solution in several languages. It's recursive and expands the meaning of the function. If the current (sub)tree contains both p and q, then the function result is their LCA. If only one of them is in that subtree, then the result is that one of them. If neither are in that subtree, the result is null/None/nil.

Update: I also wrote two iterative solutions now, one of them being a version of the solution here. They're more complicated than this simple recursive solution, but I do find them interesting.

C++

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;
    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);
    return !left ? right : !right ? left : root;
}
Python

def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right
Or using that None is considered smaller than any node:

def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    subs = [self.lowestCommonAncestor(kid, p, q)
            for kid in (root.left, root.right)]
    return root if all(subs) else max(subs)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dfs(self, root, tmp_dict, visit_arr, p, q):
        if root:
            if p in [root, root.left, root.right]:
                visit_arr[0] = True
            if q in [root, root.left, root.right]:
                visit_arr[1] = True
            if root.left:
                tmp_dict[root.left] = root
            if root.right:
                tmp_dict[root.right] = root
            if root.left and (not visit_arr[0] or not visit_arr[1]):
                self.dfs(root.left, tmp_dict, visit_arr, p, q)
            if root.right and (not visit_arr[0] or not visit_arr[1]):
                self.dfs(root.right, tmp_dict, visit_arr, p, q)

    def lCA(self, root, p, q):
        if root is None:
            return None
        elif p is None:
            return q
        elif q is None:
            return p
        tmp_dict = {}
        visit_arr = [False, False]
        self.dfs(root, tmp_dict, visit_arr, p, q)
        p_list = [p]
        while p_list[-1] in tmp_dict:
            p_list.append(tmp_dict[p_list[-1]])
        q_list = [q]
        while q_list[-1] in tmp_dict:
            q_list.append(tmp_dict[q_list[-1]])
        for item in p_list:
            if item in q_list:
                return item

    def solve2(self, root, p, q):
        # step 1: traverse
        self.memo = {root: None}
        def traverse(root):
            if root is None:
                return
            if root.left is not None:
                self.memo[root.left] = root
                traverse(root.left)
            if root.right is not None:
                self.memo[root.right] = root
                traverse(root.right)
        traverse(root)
        def back(n):
            tmplist = [n]
            while n is not None:
                n = self.memo[n]
                tmplist.append(n)
            tmplist = tmplist[:-1]
            tmplist = tmplist[::-1]
            return tmplist
            
        plist = back(p)
        qlist = back(q)
        for i in range(min(len(plist), len(qlist))):
            if plist[i] is qlist[i]:
                if i == len(plist)-1 or i == len(qlist)-1 or not plist[i+1] is qlist[i+1]:
                    return plist[i]