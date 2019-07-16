"""
1130. Minimum Cost Tree From Leaf Values (Medium)

Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

 

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
 

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
"""

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        self.memo = {}
        n = len(arr)
        self.helper(0, n-1, arr)
        _, res = self.memo[(0, n-1)]
        return res

    def helper(self, i, j, arr):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if i == j: return arr[i], 0
        if i + 1 == j:
            self.memo[(i, j)] = max(arr[i], arr[j]), arr[i] * arr[j]
            return self.memo[(i, j)]
        max_, res = None, float('inf')
        for k in range(i, j):
            max1, res1 = self.helper(i, k, arr)
            max2, res2 = self.helper(k+1, j, arr)
            res = min(res, res1 + res2 + max1 * max2)
            if max_ is None:
                max_ = max(max1, max2)
        self.memo[(i, j)] = max_, res
        return self.memo[(i, j)]


if __name__ == "__main__":
    a = Solution()
    print(a.mctFromLeafValues([2,4,2,6]))

"""
Solution DP
Find the cost for the interval [i,j].
To build up the interval [i,j],
we need to split it into left subtree and sub tree,
dp[i, j] = dp[i, k] + dp[k + 1, j] + max(A[i, k]) * max(A[k + 1, j])

This solution is O(N^3) time and O(N^2) space. You think it's fine.
After several nested for loop, you get a green accepted and release a sigh.
Then you think that's it for a medium problem,
so you didn't read and up-vote my post.

One day, you bring this solution to an interview and probably fail.

Intuition
When we build a node in the tree, we compared the two numbers a and b.
In this process,
the smaller one is removed and we won't use it anymore,
and the bigger one actually stays.

The problem can translated as following:
Given an array A, choose two neighbors in the array a and b,
we can remove the smaller one min(a,b) and the cost is a * b.
What is the minimum cost to remove the whole array until only one left?

To remove a number a, it needs a cost a * b, where b >= a.
So a has to be removed by a bigger number.
We want minimize this cost, so we need to minimize b.

b has two candidates, the first bigger number on the left,
the first bigger number on the right.

The cost to remove a is a * min(left, right).


Explanation
Now with the intuition above in mind,
we decompose a hard problem into reasonable easy one:
Just find the next greater element in the array, on the left and one right.
Refer to 1019. Next Greater Node In Linked List


Complexity
Time O(N) for one pass
Space O(N) for stack in the worst cases


Java:

    public int mctFromLeafValues(int[] A) {
        int res = 0, n = A.length;
        Stack<Integer> stack = new Stack<>();
        stack.push(Integer.MAX_VALUE);
        for (int a : A) {
            while (stack.peek() <= a) {
                int mid = stack.pop();
                res += mid * Math.min(stack.peek(), a);
            }
            stack.push(a);
        }
        while (stack.size() > 2) {
            res += stack.pop() * stack.peek();
        }
        return res;
    }
C++:

    int mctFromLeafValues(vector<int>& A) {
        int res = 0, n = A.size();
        vector<int> stack = {INT_MAX};
        for (int a : A) {
            while (stack.back() <= a) {
                int mid = stack.back();
                stack.pop_back();
                res += mid * min(stack.back(), a);
            }
            stack.push_back(a);
        }
        for (int i = 2; i < stack.size(); ++i) {
            res += stack[i] * stack[i - 1];
        }
        return res;
    }
Python:

    def mctFromLeafValues(self, A):
        res, n = 0, len(A)
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack)  >2:
            res += stack.pop() * stack[-1]
        return res
"""