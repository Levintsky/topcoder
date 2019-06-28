"""
1005. Maximize Sum Of Array After K Negations (Easy)

Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
 

Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
"""

"""
num of negatives
0. corner case: len_ = 0
1. K <= number of negatives (go positive)
 -> K-largest negative go positive
2. K > number of negatives
 2.1 K - len(neg) % 2 == 0 (all positives)
 2.2 k - len(neg) % 2 == 1 (smallest or 0 become negative)
"""

import heapq


class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 0:
            return 0
        if K == 0:
            return sum(A)
        cnt_neg = 0
        for item in A:
            if item < 0:
                cnt_neg += 1
        if cnt_neg > K:
            # heapq
            q = []
            sum_ = 0
            for item in A:
                if item < 0:
                    heapq.heappush(q, item)
                else:
                    sum_ += item
            for i in range(K):
                item = heapq.heappop(q)
                sum_ += -item  # negate large negatives
            for item in q:
                sum_ += item
            return sum_
        else:
            A = [abs(item) for item in A]
            if (K - cnt_neg) % 2 == 0:
                return sum(A)
            else:
                min_A = min(A)
                return sum(A) - 2 * min_A


if __name__ == "__main__":
    a = Solution()
    print(a.largestSumAfterKNegations([4, 2, 3], 1))
    print(a.largestSumAfterKNegations([3, -1, 0, 2], 3))
    print(a.largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
