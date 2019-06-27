"""
1043. Partition Array for Maximum Sum (Medium)

Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

Example 1:

Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]

Note:

1 <= K <= A.length <= 500
0 <= A[i] <= 10^6
"""

import bisect


class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A_ = [(-item, idx) for idx, item in enumerate(A)]
        A_.sort()
        A_ = A_[:K]
        idx = [item[1] for item in A_]
        idx.sort()
        proc = set()
        # print(idx)
        result = 0
        for item in A_:
            id_ = item[1]
            curr = bisect.bisect_left(idx, id_)
            if curr == 0:
                left = 0
            else:
                left = idx[curr - 1] + 1
                if left - 1 in proc:
                    left = id_
            if curr == len(idx) - 1:
                right = len(A) - 1
            else:
                right = idx[curr + 1] - 1
                if right + 1 in proc:
                    right = id_
            val = A[id_]
            for i in range(left, right + 1):
                A[i] = val
            result += (right - left + 1) * A[id_]
            proc.add(id_)
        print(A, sum(A))
        return result

    def solve2(self, A, K):
        # dp:
        # result[i]: best until i
        # and choose the one with minimum length of last partition
        # iterate after a new item is added
        N = len(A)
        dp = [0] * (N + K)
        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[N - 1]


if __name__ == "__main__":
    a = Solution()
    # print(a.maxSumAfterPartitioning([1,15,7,9,2,5,10], 3))
    print(a.solve2([1, 15, 7, 9, 2, 5, 10], 3))
    # print(a.maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3], 4))
