"""
1483. Kth Ancestor of a Tree Node (Hard)

You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of node i. The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there is no such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to the root.

 

Example:



Input:
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

Output:
[null,1,0,-1]

Explanation:
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2);  // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3);  // returns -1 because there is no such ancestor
 

Constraints:

1 <= k <= n <= 5*10^4
parent[0] == -1 indicating that 0 is the root node.
0 <= parent[i] < n for all 0 < i < n
0 <= node < n
There will be at most 5*10^4 queries.
"""


class TreeAncestor(object):

    step = 15
    def __init__(self, n, A):
        A = dict(enumerate(A))
        jump = [A]
        for s in xrange(self.step):
            B = {}
            for i in A:
                if A[i] in A:
                    B[i] = A[A[i]]
            jump.append(B)
            A = B
        self.jump = jump

    def getKthAncestor(self, x, k):
        step = self.step
        while k > 0 and x > -1:
            if k >= 1 << step:
                x = self.jump[step].get(x, -1)
                k -= 1 << step
            else:
                step -= 1
        return x
"""

class TreeAncestor(object):

    def __init__(self, n, parent):
        curr = dict(enumerate(parent))
        self.jump = [curr]
        while True:
            memo = {}
            curr = self.jump[-1] # current dict
            for k, p in curr.items():
                if p in curr:
                    memo[k] = curr[p]
            if len(memo) == 0:
                break
            else:
                self.jump.append(memo)
        # self.step = len(self.jump)

    def getKthAncestor(self, node, k):
        step = len(self.jump) - 1
        while step >= 0 and k >= 0:
            if 1 << step <= k:
                k -= 1 << step
                node = self.jump[step].get(node, -1)
            step -= 1
            if node == -1:
                return -1
        if k == 0:
            return node
        else:
            return -1
"""



# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

if __name__ == "__main__":
    """
    a = TreeAncestor(7,[-1,0,0,1,1,2,2])
    for i, j in [[3,1],[5,2],[6,3]]:
        print(a.getKthAncestor(i, j))

    a = TreeAncestor(5,[-1,0,0,0,3])
    for i, j in [[1,5],[3,2],[0,1],[3,1],[3,5]]:
        print(a.getKthAncestor(i, j))
    """

    a = TreeAncestor(5,[-1,0,0,1,2])
    for i, j in [[3,5],[3,2],[2,2],[0,2],[2,1]]:
        print(a.getKthAncestor(i, j))
