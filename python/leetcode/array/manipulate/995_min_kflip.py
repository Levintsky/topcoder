"""
995. Minimum Number of K Consecutive Bit Flips (Hard)

In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].

Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].

Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]

Note:

1 <= A.length <= 30000
1 <= K <= A.length
"""


class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # TLE
        cnt = 0
        for i in range(len(A) - K + 1):
            if A[i] == 0:
                cnt += 1
                for j in range(i, i + K):
                    A[j] = 1 - A[j]
        if sum(A) == len(A):
            return cnt
        else:
            return -1

    def solution2(self, A, K):
        n = len(A)
        flipped = 0
        res = 0
        isFlipped = [0] * n
        for i in range(n):
            if i >= K:
                flipped ^= isFlipped[i - K]
            if flipped == A[i]:
                if i + K > n:
                    return -1
                isFlipped[i] = 1
                flipped ^= 1
                res += 1
        return res


if __name__ == "__main__":
    a = Solution()
    # print(a.minKBitFlips([0,1,0], 1))
    # print(a.minKBitFlips([1,1,0], 2))
    print(a.solution2([0, 0, 0, 1, 0, 1, 1, 0], 3))
