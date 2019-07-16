"""
974. Subarray Sums Divisible by K (Medium)

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 
Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        memo = {0: [-1]}
        tmp = 0
        res = 0
        for i, item in enumerate(A):
            tmp = (tmp + item) % K
            if tmp in memo:
                res += len(memo[tmp])
            if tmp not in memo:
                memo[tmp] = []
            memo[tmp].append(i)
        return res

    def solve(self, A, K):
        memo = [0] * K
        memo[0] = 1
        tmp = 0
        res = 0
        for i, item in enumerate(A):
            tmp = (tmp + item) % K
            res += memo[tmp]
            memo[tmp] += 1
        return res
