"""
1031. Maximum Sum of Two Non-Overlapping Subarrays (Medium)

Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.

Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.

Note:

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
"""


class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        # result1[i]: max sum of [A[0:L], A[1:L+1], A[i:L+i]]
        result1 = self.helper(A, L)
        # result2[j]: max sum of [A[j:j+M], A[n-M-1:n-1], A[n-M:n]]
        result2 = self.helper_right(A, M)
        print(result1)
        print(result2)
        curr = result1[0] + result2[L]
        i = 0
        while i < len(result1) and i + L < len(result2):
            curr = max(curr, result1[i] + result2[L + i])
            i += 1
        print(curr)
        result1 = self.helper(A, M)
        result2 = self.helper_right(A, L)
        print(result1)
        print(result2)
        i = 0
        while i < len(result1) and i + M < len(result2):
            print(i, result1[i], result2[M + i])
            curr = max(curr, result1[i] + result2[M + i])
            i += 1
        return curr

    def helper(self, A, l):
        n = len(A)
        result = [sum(A[:l])]
        curr = result[-1]
        for i in range(l, n):
            curr = curr + A[i] - A[i - l]
            if curr > result[-1]:
                result.append(curr)
            else:
                result.append(result[-1])
        return result

    def helper_right(self, A, l):
        n = len(A)
        result = [sum(A[n - l :])]
        curr = result[-1]
        for i in range(n - l - 1, -1, -1):
            curr = curr + A[i] - A[i + l]
            if curr > result[-1]:
                result.append(curr)
            else:
                result.append(result[-1])
        result = result[::-1]
        return result


if __name__ == "__main__":
    a = Solution()
    # print(a.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2))
    # print(a.maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0], 3, 2))
    print(a.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))
