"""
823. Binary Trees With Factors (Medium)

Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:

Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

Note:

1 <= A.length <= 1000.
2 <= A[i] <= 10 ^ 9.
"""

class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        memo = {A[0]: 1}
        res = 1
        MOD = 10 ** 9 + 7
        for item in A[1:]:
            tmpres = 1 # itself
            for k1 in memo.keys():
                if item % k1 != 0:
                    continue
                k2 = item // k1
                if k2 in memo:
                    tmpres += memo[k1] * memo[k2]
            memo[item] = tmpres % MOD
            res = (res + tmpres) % MOD
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.numFactoredBinaryTrees([2, 4]))
    print(a.numFactoredBinaryTrees([2, 4, 5, 10]))
    print(a.numFactoredBinaryTrees([2, 4, 8]))
